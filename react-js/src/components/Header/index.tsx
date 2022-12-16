import classNames from 'classnames';
import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import styles from "./Header.module.scss";
import { MdOutlineLibraryMusic, MdOutlineModeEditOutline, MdOutlineHome } from "react-icons/md";
import { RiMenuUnfoldLine, RiMenuLine } from "react-icons/ri";
import { useRecoilState, useSetRecoilState } from 'recoil';
import { userInfoAtom } from 'states/user';
import { jwtTokenAtom } from 'states/jwtToken';
import axios from 'axios'; 
import { useCookies } from 'react-cookie';
import { librarysAtom } from 'states/librarys';
import { resetUserInfo } from 'utils/_resetUserInfo';
import NavButton from './components/NavButton';
import { TMusics } from 'types/musicsType';
import Recomendations from './components/Recomendations';


export default function Header() {
    const [menuActive, useMenuActive] = useState(false);
    const [loadedState, setLoadedState] = useState(false);
    const [musicsState, setMusicsState] = useState<TMusics[]>();

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const [userInfoState, setUserInfoState] = useRecoilState(userInfoAtom);
    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);


    let headerStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['menu_color']
    } as React.CSSProperties : {} as React.CSSProperties;

    let buttonStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['button_color'],
        textColor: userInfoState['color_configs']['text_color']
    } as React.CSSProperties : {} as React.CSSProperties;

    let nameStyle = userInfoState ? {
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let hambuguerStyle = userInfoState ? {
        color: userInfoState['color_configs']['button_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    const navigate = useNavigate();


    function _CheckLogin() {
        if(cookies.token !== null && cookies.token !== "" && cookies.token !== undefined && cookies.token !== "/") {
            setJwtTokenState((_) => cookies.token);
        }
        else {
            _Logout();
        }
    }

    function _Logout() {
        setLibrarysState((_) => []);
        setUserInfoState((_) => resetUserInfo());
        setJwtTokenState((_) => "");
        removeCookie('token', { path: '/'});
        navigate("/");
    }

    function RecomendMusic() {
        axios.get('http://fjackson.pythonanywhere.com/catalog/list/').then(response => {
            setMusicsState((_) => response.data['results']);
        }).catch(e => {
            _Logout();
        });
    }

    function GetUserInfo() {
        if(jwtTokenState) {
            axios.get('https://fjackson.pythonanywhere.com/user/', {
                headers: {
                    'token': jwtTokenState
                }
            }).then((response) => {
                setUserInfoState((_) => response.data['user']);
            }).catch((error) => {
                _Logout();
            });
        }
    }

    function ActiveMenu() {
        useMenuActive(!menuActive)
    }

    useEffect(() => {
        _CheckLogin();
    }, []);

    useEffect(() => {
        GetUserInfo();
        RecomendMusic();
    }, [jwtTokenState]);

    
    useEffect(() => {
        if (!loadedState) {
            if ('token' in cookies) {
                setJwtTokenState((_) => cookies['token'])
            }
        }
        setLoadedState((_) => true);
    }, [loadedState, cookies, setJwtTokenState])

    return (
        <header 
            className={classNames({
                [styles.header]: true,
                [styles["header-desactive"]]: !menuActive
            })}
            style={headerStyle}
        >
            <RiMenuUnfoldLine 
                className={classNames({
                    [styles.hambuger__button]: true,
                    [styles['hambuger__button-desative']]: !menuActive
                })} 
                onClick={() => ActiveMenu()} 
                style={hambuguerStyle}
            />
            <RiMenuLine 
                className={classNames({
                    [styles.hambuger__button]: true,
                    [styles['hambuger__button-active']]: menuActive
                })} 
                onClick={() => ActiveMenu()} 
                style={hambuguerStyle}
            />
            {
                userInfoState['username'] !== '' ? 
                <>
                    <div className={styles.user}>
                        <img src={process.env.PUBLIC_URL + '../assets/img/user-image.webp'} alt="Your user"/>
                        <div
                            className={styles.user__info}
                        >
                            <p
                                style={nameStyle}
                            >
                                {userInfoState ? userInfoState['username'] : 'SpofityAi'}
                            </p>
                            <Link
                                to="configs"
                                style={buttonStyle}
                            >
                                <MdOutlineModeEditOutline className={styles.edit__icon}/>
                            </Link>
                        </div>
                    </div>
                    <nav className={styles.links}> 
                        <NavButton 
                            link={"/"}
                            text={"Home"}
                        >
                            <MdOutlineHome />
                        </NavButton>
                        <NavButton 
                            link={"librarys/"}
                            text={"My Librarys"}
                        >
                            <MdOutlineLibraryMusic /> 
                        </NavButton>
                    </nav>
                    {
                        menuActive ?
                        <Recomendations 
                            musics={musicsState}
                        />
                        : 
                        <></>
                    }
                </>
                :
                <div className={styles.spotify__image__container}>
                    <img 
                        src={process.env.PUBLIC_URL + 'assets/img/spotify.png'} 
                        alt="Spotify Logo"
                    />
                    <p>
                        Enjoy your musics
                    </p>
                </div>
            }
        </header>
    );
}