import axios from "axios";
import { useEffect, useRef, useState } from "react";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";
import { useSetRecoilState, useRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import { librarysAtom } from "states/librarys";
import { searchMusicsAtom } from "states/searchMusics";
import { userInfoAtom } from "states/user";
import { TMusics } from "types/musicsType";
import { resetUserInfo } from "utils/_resetUserInfo";
import Music from "./Music";
import styles from "./SearchMusics.module.scss";


export default function SearchMusics() {
    const listInnerRef = useRef(null);
    const [searchMusicsState, setSearchMusicsState] = useRecoilState(searchMusicsAtom);
    const [musicsListState, useMusicsListState] = useState<TMusics[]>();
    const [musicsListLenghtState, useMusicsListLenghtState] = useState(6);
    const setLibrarysState = useSetRecoilState(librarysAtom);
    const setUserInfoState = useSetRecoilState(userInfoAtom);
    const setJwtTokenState =  useSetRecoilState(jwtTokenAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();


    function _Logout() {    
        setLibrarysState((_) => []);
        setUserInfoState((_) => resetUserInfo());
        setJwtTokenState((_) => "");
        removeCookie('token', { path: '/'});
        navigate("/");
    }

    function _GetMusics(musics: TMusics[]) {
        setSearchMusicsState((_) => musics)
        useMusicsListState((_) => musics.slice(0, musicsListLenghtState));
    }

    function loadMoreMusics() {
        if (listInnerRef.current) {
            const { scrollTop, scrollHeight, clientHeight } = listInnerRef.current;
            
            if (scrollTop + clientHeight === scrollHeight) {
                _AddMoreLenghtMusicList();
            }
        }
    }
    
    function _AddMoreLenghtMusicList() {
        useMusicsListLenghtState((old) => old + 6);
    }

    function ResetMusicsList() {
        useMusicsListLenghtState((_) => 6);
        HandleMusicsList();
    }

    function HandleMusicsList() {
        const musicsList = searchMusicsState.length >= musicsListLenghtState ? searchMusicsState.slice(0, musicsListLenghtState) : searchMusicsState;
        useMusicsListState((_) => musicsList);
    }

    useEffect(() => {
        ResetMusicsList();
    }, [searchMusicsState]);

    useEffect(() => {
        HandleMusicsList();
    }, [musicsListLenghtState]);

    useEffect(() => {
        axios.get('http://fjackson.pythonanywhere.com/catalog/list/').then(response => {
            _GetMusics(response.data['results']);
        }).catch(e => {
            _Logout();
        });
    }, []);


    return (
        <div className={styles.searchMusics__container}>
            <ul
                className={styles.musics__list}
                onScroll={(_) => loadMoreMusics()}
                ref={listInnerRef}
            >
                {musicsListState?.map((searchMusic) => 
                    <li
                        key={searchMusic.id}
                    >
                        <Music 
                            name={searchMusic.name}
                            author={searchMusic.author}
                            id={searchMusic.id}
                            genre={searchMusic.genre}
                            search={searchMusic.search}
                            track_id={searchMusic.track_id}
                            cluster_class={searchMusic.cluster_class}
                        />
                    </li>
                )}
            </ul>
        </div>
    );
}