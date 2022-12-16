import axios from "axios";
import Button from "components/Button";
import { useCookies } from "react-cookie";
import { RiHeartAddLine } from "react-icons/ri";
import { useNavigate, useParams } from "react-router-dom";
import { useRecoilState, useSetRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import { librarysAtom } from "states/librarys";
import { musicsInLibraryAtom } from "states/musicsInLibrary";
import { userInfoAtom } from "states/user";
import { resetUserInfo } from "utils/_resetUserInfo";
import styles from "./Music.module.scss";
import { TMusics } from "types/musicsType";
import { searchMusicsAtom } from "states/searchMusics";


export default function Music(props: TMusics) {
    const [musicsState, setMusicsState] = useRecoilState(musicsInLibraryAtom);
    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);
    const [searchMusicsState, setSearchMusicsState] = useRecoilState(searchMusicsAtom);
    const [userInfoState, setUserInfoState] = useRecoilState(userInfoAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const { id } = useParams();

    const navigate = useNavigate();

    let musicStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['music_background_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let textStyle = userInfoState ? {
        textColor: userInfoState['color_configs']['text_color']
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

    function favMusic() {
        const url = `https://fjackson.pythonanywhere.com/librarys-musics/${id}/`
        const data = {
            "musics_ids_to_put": [props.id]
        }

        axios.put(url, data, {
            headers: {
                'token': jwtTokenState
            }
        }).then(response => {
            _GetToken(response.data);

            const music = props

            const musicsFilter = musicsState.filter(musicF => (
                musicF.id === music.id
            ))
            
            if(musicsFilter.length === 0) {
                setMusicsState((oldMusics) => [...oldMusics, music])
            }

            const searchMusics = searchMusicsState.filter(searchMusic => searchMusic.id !== music.id)

            setSearchMusicsState((_) => searchMusics);
        }).catch(e => {
            _Logout();
        });
    }

    return (
        <article 
            className={styles.music}
            style={musicStyle}
        >
            <img src={process.env.PUBLIC_URL + '../assets/img/music-image.webp'} alt="music" className={styles.music_image}/>
            <p 
                className={styles.music__title}
                style={textStyle}
            >
                {props.name}
            </p>
            <p 
                className={styles.music__author}
                style={textStyle}
            >
                {props.author}
            </p>
            <Button 
                onClick={() => favMusic()}
            >
                {<RiHeartAddLine />}
            </Button>
        </article>
    );
}