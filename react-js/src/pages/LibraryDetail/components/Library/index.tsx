import Music from "./components/Music";
import { FaRandom } from "react-icons/fa";
import { HiArrowDownOnSquareStack, HiArrowUpOnSquare } from "react-icons/hi2";
import { useEffect, useState } from "react";

import styles from "./Library.module.scss";
import classNames from "classnames";
import axios from "axios";
import { jwtTokenAtom } from "states/jwtToken";
import { useRecoilState, useRecoilValue, useSetRecoilState } from "recoil";
import { useCookies } from "react-cookie";
import { resetUserInfo } from "utils/_resetUserInfo";
import { useNavigate } from "react-router-dom";
import { userInfoAtom } from "states/user";
import { librarysAtom } from "states/librarys";
import { musicsInLibraryAtom } from "states/musicsInLibrary";


type TMusicMenuState = "closed" | "open";

interface Props {
    id: string | undefined,
    loadedState: boolean
}


export default function Library(props: Props) {
    const [musicMenuState, setMusicMenuState] = useState<TMusicMenuState>("open");
    const [titleState, setTitleState] = useState('');
    
    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);

    const musicsState = useRecoilValue(musicsInLibraryAtom);

    const [userInfoState, setUserInfoState] = useRecoilState(userInfoAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();

    let libraryStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['menu_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let dropDownStyle = userInfoState ? {
        borderColor: userInfoState['color_configs']['button_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let iconStyle = userInfoState ? {
        color: userInfoState['color_configs']['button_color']
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

    function _GetLibraryDetails() {
        axios.get(`https://fjackson.pythonanywhere.com/librarys/${props.id}/`, {
            headers: {
                'token': jwtTokenState
            }
        }).then(response => {
            _GetToken(response.data);
            setTitleState((_) => response.data['library'].name);
        }).catch(e => {
            _Logout();
        });
    }

    function changeMusicMenu() {
        if (musicMenuState === "closed"){
            setMusicMenuState("open");
        }
        else {
            setMusicMenuState("closed");
        }
    }
    
    useEffect(() => {
        if(props.loadedState) {
            _GetLibraryDetails();
        }
    }, [props.loadedState]);


    return (
        <div 
            className={styles.library}
            style={libraryStyle}
        >
            <h2 className={styles.library__title}>{titleState}</h2>
            <div className={styles.library__image__container}>
                <img src={process.env.PUBLIC_URL + '../assets/img/library-image.webp'} alt="" className={styles.library__image}/>
            </div>
            <div>
                <div>
                    <button 
                        className={styles.library__musics__open}
                        onClick={() => changeMusicMenu()}
                        style={dropDownStyle}
                    >
                        {
                            musicMenuState === "closed" ? 
                            <HiArrowDownOnSquareStack 
                                className={styles.library__musics__open__icon}
                                style={iconStyle}
                            /> 
                            : 
                            <HiArrowUpOnSquare 
                                className={styles.library__musics__open__icon}
                                style={iconStyle}
                            />
                        }
                        Musics
                    </button>
                </div>
                <ul className={classNames({
                    [styles.library__musics__list]: true,
                    [styles["library__musics__list-open"]]: musicMenuState === "open"
                })}>
                    {musicsState?.map(music =>                     
                        <li
                            key={music.id}
                        >
                            <Music 
                                title={music.name}
                                author={music.author}
                                link={music.track_id}
                                id={music.id}
                            />
                        </li>)}
                </ul>
            </div>
        </div>
    );
}