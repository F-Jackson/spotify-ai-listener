import styles from "./AddNewLibrary.module.scss";
import { MdOutlineAddAPhoto } from "react-icons/md";
import Button from "components/Button";
import Input from "components/Inputs";
import { useState } from "react";
import axios from "axios";
import { useRecoilState, useSetRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import { resetUserInfo } from "utils/_resetUserInfo";
import { userInfoAtom } from "states/user";
import { librarysAtom } from "states/librarys";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";


interface Props {
    refreshLibrarysList: () => void
}

export default function AddNewLibrary(props: Props) {
    const [titleState, setTitleState] = useState('');

    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);
    const [userInfoState, setUserInfoState] = useRecoilState(userInfoAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();

    let addNewLibraryStyle = userInfoState ? {
        borderColor: userInfoState['color_configs']['button_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let iconStyle = userInfoState ? {
        color: userInfoState['color_configs']['button_color'],
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

    function AddNewLibrary(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();

        if(!jwtTokenState) {
            return;
        }

        axios.put('https://fjackson.pythonanywhere.com/librarys/', {
            name: titleState
        }, {
            headers: {
                'token': jwtTokenState
            }
        }).then(response => {
            _GetToken(response.data);
            props.refreshLibrarysList();
        }).catch(error => {
            if('token' in error.response.data) {
                const data = error.response.data;
        
                _GetToken(data);
                props.refreshLibrarysList();
            }
            else {
                _Logout();
            }
        });
    }

    return (
        <form 
            className={styles.add__new} 
            action=""
            onSubmit={AddNewLibrary}
        >
            <div 
                className={styles.playlist__img}
            >
                <input
                    type="file" 
                    name="new__playlist__image"
                    id="new__playlist__image"
                    title="Image for the new playlist"
                    accept="image/*"
                    className={styles.new__playlist__img}
                    hidden
                />
                <label 
                    htmlFor="new__playlist__image"
                    style={addNewLibraryStyle}
                >
                    <MdOutlineAddAPhoto
                        className={styles.playlist__img__icon}
                        style={iconStyle}
                    />
                </label>
            </div>
                <Input
                    type="text"
                    name="new_playlist"
                    placeholder="Playlist title"
                    value={titleState}
                    onChange={(e) => setTitleState(e.currentTarget.value)}
                />
                <Button
                    type="submit"
                >
                    Add
                </Button>
        </form>
    );
}