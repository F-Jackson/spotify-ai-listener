import axios from "axios";
import Button from "components/Button";
import { useState } from "react";
import { MdOutlineSearch } from "react-icons/md";
import { useRecoilValue, useSetRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import { musicsInLibraryAtom } from "states/musicsInLibrary";
import { searchMusicsAtom } from "states/searchMusics";
import { userInfoAtom } from "states/user";
import { TMusics } from "types/musicsType";

import styles from "./SearchBar.module.scss";


export default function SearchBar() {
    const [searchTextState, setSearchTextState] = useState('');
    const setSearchMusicsState = useSetRecoilState(searchMusicsAtom);

    const musicsInLibrary = useRecoilValue(musicsInLibraryAtom);
    const jwtTokenState =  useRecoilValue(jwtTokenAtom);
    const userInfoState = useRecoilValue(userInfoAtom);

    let inputStyle = userInfoState ? {
        borderColor: userInfoState['color_configs']['button_color']
    }  as React.CSSProperties : {} as React.CSSProperties;
    

    function _SetSearchMusic(responseData: TMusics[]) {
        let musics: TMusics[] = responseData;

        const musicsInLibraryIds = musicsInLibrary.map(music => music.id);

        musics = musics.filter(music => !musicsInLibraryIds.includes(music.id));

        setSearchMusicsState((_) => musics);
    }

    function _searchMusics(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();

        axios.post("https://fjackson.pythonanywhere.com/catalog/", {
            'mode': 'search',
            'search_text': searchTextState
        }, {
            headers: {
                'token': jwtTokenState
            }
        }).then(response => {
            _SetSearchMusic(response.data);
        }).catch(e => {
            setSearchMusicsState((_) => []);
        })
    }

    function _recomendMusics() {
        let genres: any = {};
        let clusters: any = {};

        musicsInLibrary.forEach((music) => {
            music.genre in genres ? genres[music.genre] += 5 : genres[music.genre] = 5;
            music.cluster_class in clusters ? clusters[music.cluster_class] += 5 : clusters[music.cluster_class] = 5;
        });

        const data = {
            'mode': 'recomend',
            'genres': genres,
            'clusters': clusters
        }

        axios.post("https://fjackson.pythonanywhere.com/catalog/", data, 
        {
            headers: {
                'token': jwtTokenState
            }
        }).then(response => {
            _SetSearchMusic(response.data);
        }).catch(e => {
            setSearchMusicsState((_) => []);
        })
    }

    function handleInputChange(inputValue: string) {
        setSearchTextState(inputValue);

        if (inputValue === null || inputValue === undefined || inputValue === '') {
            _recomendMusics();
        }
    }
    
    return (
        <div className={styles.searchBar__container}>
            <form 
                action=""
                className={styles.searchBar}
                onSubmit={(e) => _searchMusics(e)}
            >
                <input 
                    type="text"
                    placeholder="Search for your music"
                    title="search music"
                    className={styles.searchBar__input}
                    value={searchTextState}
                    onChange={(e) => handleInputChange(e.currentTarget.value)}
                    style={inputStyle}
                />
                <Button
                    type="submit"
                >
                    <MdOutlineSearch />
                </Button>
            </form>
        </div>
    );
}