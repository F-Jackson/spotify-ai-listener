import axios from "axios";
import { useCookies } from "react-cookie";
import { HiPlayPause } from "react-icons/hi2";
import { TbTrashX } from "react-icons/tb";
import { useNavigate, useParams } from "react-router-dom";
import { useRecoilState, useSetRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import { librarysAtom } from "states/librarys";
import { musicsInLibraryAtom } from "states/musicsInLibrary";
import { userInfoAtom } from "states/user";
import { resetUserInfo } from "utils/_resetUserInfo";
import styles from "./Music.module.scss";


interface Props {
    title: string,
    author: string,
    link: string,
    id: number
}

export default function Music(props: Props) {
    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);
    const [userInfoState, setUserInfoState] = useRecoilState(userInfoAtom);
    const [musicsState, setMusicsState] = useRecoilState(musicsInLibraryAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();

    const { id } = useParams();

    let musicStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['music_background_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let textStyle = userInfoState ? {
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let iconStyle = userInfoState ? {
        color: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let buttonStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['button_color']
    }  as React.CSSProperties : {} as React.CSSProperties;
    

    function _GetToken(data: any) {
        const token: string = data['token'];
    
        setJwtTokenState((_) => token);
        setCookie('token', token, { path: '/' });
    }

    function _Logout() {    
        setLibrarysState((_) => []);
        setUserInfoState((_) => resetUserInfo());
        setJwtTokenState((_) => "");
        removeCookie('token', { path: '/'});
        navigate("/");
    }

    function deleteMusic() {
        const url = `https://fjackson.pythonanywhere.com/librarys-musics/${id}/`
        const data = {
            "musics_ids_to_delete": [props.id]
        }

        axios.delete(url, {
            headers: {
                'token': jwtTokenState
            },
            data: data
        }).then(response => {
            console.log(response);
            _GetToken(response.data);

            const music = props

            const musicsFilter = musicsState.filter(musicF => (
                musicF.id !== music.id
            ))
            
            setMusicsState((_) => musicsFilter)
        }).catch(e => {
            _Logout();
        });
    }

    function openMusic(link: string): void{
        window.open(`https://open.spotify.com/track/${link}`)
    }

    return (
        <article 
            className={styles.music__container}
            style={musicStyle}
        >
            <button
                className={styles.delete__button}
                onClick={() => {deleteMusic()}}
                style={buttonStyle}
            >
                {<TbTrashX 
                    style={iconStyle}
                />}
            </button>
            <p 
                className={styles.music__title}
                style={textStyle}
            >
                {props.title}
            </p>
            <p 
                className={styles.musics__author}
                style={textStyle}
            >
                {props.author}
            </p>
            <button
                className={styles.play__button}
                onClick={() => {openMusic(props.link)}}
                style={buttonStyle}
            >
                {<HiPlayPause style={iconStyle}/>}
            </button>
        </article>
    );
}