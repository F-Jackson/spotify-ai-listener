import axios from "axios";
import { useEffect, useState } from "react";
import { useCookies } from "react-cookie";
import { useNavigate, useParams } from "react-router-dom";
import { useSetRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import { librarysAtom } from "states/librarys";
import { musicsInLibraryAtom } from "states/musicsInLibrary";
import { userInfoAtom } from "states/user";
import { resetUserInfo } from "utils/_resetUserInfo";
import Library from "./components/Library"
import SearchBar from "./components/SearchBar"
import SearchMusics from "./components/SearchMusics"
import styles from "./LibraryDetail.module.scss";


export default function LibraryDetail() {
    const [loadedState, setLoadedState] = useState(false);


    const setMusicsState = useSetRecoilState(musicsInLibraryAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);
    const setUserInfoState = useSetRecoilState(userInfoAtom);
    const setJwtTokenState =  useSetRecoilState(jwtTokenAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();
    const { id } = useParams();

    function _GetMusics() {
        const url = `https://fjackson.pythonanywhere.com/librarys-musics/${id}/`
        axios.get(url, {
            headers: {
                'token': cookies.token
            }
        }).then(response => {
            _GetToken(response.data);

            const musics = response.data['musics'];
            setMusicsState((_) => musics);
        }).catch(error => {
            _Logout();
        });
    }

    function _CheckLogin() {
        if(cookies.token !== null && cookies.token !== "" && cookies.token !== undefined && cookies.token !== "/") {
            setJwtTokenState((_) => cookies.token);
        }
        else {
            _Logout();
        }
    }

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

    useEffect(() => {
        if(!loadedState) {
            _CheckLogin();
            setLoadedState((_) => true);
            _GetMusics();
        }
    }, []);

    return (
        <div className={styles.libraryDetail__container}>
            <section className={styles.library__container}>
                <Library 
                    id={id}
                    loadedState={loadedState}
                />
            </section>
            <section className={styles.other__musics}>
                <SearchBar />
                <SearchMusics />
            </section>
        </div>
    )
}