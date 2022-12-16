import axios from "axios";
import { useEffect } from "react";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";
import { useRecoilState, useSetRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import { librarysAtom } from "states/librarys";
import { userInfoAtom } from "states/user";
import { resetUserInfo } from "utils/_resetUserInfo";
import AddNewLibrary from "./components/AddNewLibrary";
import Library from "./components/Library";
import styles from "./LibraryList.module.scss";


export default function LibraryList() {
    const [librarysState, setLibrarysState] = useRecoilState(librarysAtom);
    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);
    const setUserInfoState = useSetRecoilState(userInfoAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();

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

    function ListUserLibrarys() {
        if(!jwtTokenState) {
            return;
        }

        axios.get('https://fjackson.pythonanywhere.com/librarys/', {
            headers: {
                'token': jwtTokenState
            }
        }).then(response => {
            if('librarys' in response.data) {
                const librarys: [] = response.data['librarys'];

                setLibrarysState((_) => librarys);
            }

            _GetToken(response.data);
        }).catch(error => {
            if('token' in error.response.data) {
                const data = error.response.data;
                
                _GetToken(data);
            }
            else {
                _Logout();
            }
        })
    }

    useEffect(() => {
        _CheckLogin();
    }, []);

    useEffect(() => {
        ListUserLibrarys();
    }, [jwtTokenState]);

    return (
        <section className={styles.libraryList__container}>
            <ul className={styles.library__list}>
                {
                    librarysState.map(library => (
                        <li
                            key={library['id']}
                        >
                            <Library 
                                title={library['name']}
                                id={library['id']}
                                refreshLibrarysList={ListUserLibrarys}
                            />
                        </li>
                    ))
                }
                <li>
                    <AddNewLibrary refreshLibrarysList={ListUserLibrarys}/>
                </li>
            </ul>
        </section>
    );
}