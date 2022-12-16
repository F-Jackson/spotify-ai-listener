import { TbTrashX } from "react-icons/tb";
import { BsFillPlayFill } from "react-icons/bs";
import styles from "./Library.module.scss";
import { useRecoilState, useSetRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import { librarysAtom } from "states/librarys";
import { useCookies } from "react-cookie";
import { resetUserInfo } from "utils/_resetUserInfo";
import { userInfoAtom } from "states/user";


interface Props {
    title: string,
    id: number,
    refreshLibrarysList: () => void
}

export default function Library(props: Props) {
    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);
    const [librarysState, setLibrarysState] = useRecoilState(librarysAtom);
    const [userInfoState, setUserInfoState] = useRecoilState(userInfoAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();

    let libraryStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['music_background_color'],
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let titleStyle = userInfoState ? {
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let buttonStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['button_color'],
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let iconStyle = userInfoState ? {
        color: userInfoState['color_configs']['text_color']
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

    function DeleteMusic() {
        if(!jwtTokenState) {
            return;
        }

        axios.delete(`https://fjackson.pythonanywhere.com/librarys/${props.id}`, {
            headers: {
                'token': jwtTokenState
            }
        }).then(response => {
            _GetToken(response.data);
            props.refreshLibrarysList();
        }).catch(e => {
            _Logout();
            props.refreshLibrarysList();
        });
    }


    return (
        <article 
            className={styles.library}
            style={libraryStyle}
        >
            <h2 
                className={styles.title}
                style={titleStyle}
            >
                {props.title}
            </h2>
            <img 
                src={process.env.PUBLIC_URL + '../assets/img/library-image.webp'} 
                alt="Library"
                className={styles.image}
            />
            <Link 
                className={styles.play}
                to={`/library/${props.id}`}
                style={buttonStyle}
            >
                <BsFillPlayFill />
            </Link>
            <button 
                className={styles.delete} 
                title="play music"
                onClick={(e) => DeleteMusic()}
                style={buttonStyle}
            >
                <TbTrashX 
                    style={iconStyle}
                />
            </button>
        </article>
    );
}