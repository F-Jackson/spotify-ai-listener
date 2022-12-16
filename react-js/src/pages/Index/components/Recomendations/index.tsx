import axios from "axios";
import { useEffect, useState } from "react";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";
import { useSetRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import { librarysAtom } from "states/librarys";
import { userInfoAtom } from "states/user";
import { TMusics } from "types/musicsType";
import { resetUserInfo } from "utils/_resetUserInfo";
import Musics from "./components/Musics";
import styles from "./Recomendations.module.scss";

export default function Recomendations() {
    const [musicsState, setMusicsState] = useState<TMusics[]>();

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const setUserInfoState = useSetRecoilState(userInfoAtom);
    const setJwtTokenState =  useSetRecoilState(jwtTokenAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);

    const navigate = useNavigate();

    function _Logout() {
        setLibrarysState((_) => []);
        setUserInfoState((_) => resetUserInfo());
        setJwtTokenState((_) => "");
        removeCookie('token', { path: '/'});
        navigate("/");
    }

    function _GetMusics() {
        axios.get('http://fjackson.pythonanywhere.com/catalog/list/').then(response => {
            setMusicsState((_) => response.data['results']);
        }).catch(e => {
            _Logout();
        });
    }

    useEffect(() => {
        _GetMusics();
    }, []);
    
    return (
        <section className={styles.musics__container}>
            <ul className={styles.musics__list}>
                {
                    musicsState?.map(music => (
                        <li
                            key={music.id}
                        >
                            <Musics 
                                name={music.name}
                                genre={music.genre}
                                track_id={music.track_id}
                            />
                        </li>
                    ))
                }
            </ul>
        </section>
    );
}