import Input from "components/Inputs";
import Select from "./components/Select";
import countryCodes from "data/country-codes.json";
import genres from "data/genres.json";
import styles from "./Configs.module.scss";
import classNames from "classnames";
import Button from "components/Button";
import { useEffect, useState } from "react";
import { useRecoilState, useSetRecoilState } from "recoil";
import { userInfoAtom } from "states/user";
import axios from "axios";
import { jwtTokenAtom } from "states/jwtToken";
import { useCookies } from "react-cookie";
import { resetUserInfo } from "utils/_resetUserInfo";
import { librarysAtom } from "states/librarys";
import { useNavigate } from "react-router-dom";


type userInfoType = {
        username: string,
        email: string,
        first_name: string,
        second_name: string,
        genre: string,
        country_code: string,
        color_configs: {
            background_color: string,
            menu_color: string,
            button_color: string,
            text_color: string,
            music_background_color: string
        }
    }


export default function Configs() {
    const [usernameState, setUsernameState] = useState('');
    const [emailState, setEmailState] = useState('');
    const [firstNameState, setFirstNameState] = useState('');
    const [secondNameState, setSecondNameState] = useState('');
    const [countryCodeState, setCountryCodeState] = useState('');
    const [genreState, setGenreState] = useState('');
    const [backgroundColorState, setBackgroundColorState] = useState('');
    const [menuColorState, setMenuColorState] = useState('');
    const [buttonColorState, setButtonColorState] = useState('');
    const [textColorState, setTextColorState] = useState('');
    const [musicBackgroundColorState, setMusicBackgroundColorState] = useState('');

    const [userInfoState, setUserInfoState] = useRecoilState(userInfoAtom);
    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);

    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();

    let inputStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['button_color'],
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;


    function _CheckLogin() {
        if(cookies.token !== null && cookies.token !== "" && cookies.token !== undefined && cookies.token !== "/") {
            setJwtTokenState((_) => cookies.token);
        }
        else {
            _Logout();
        }
    }

    useEffect(() => {
        _CheckLogin();
    }, []);

    function _getGeoInfo() {
        axios.get('https://ipapi.co/json/').then((response) => {
            const data = response.data;
            const countryCodeNumber = data['country_calling_code'].replace(/\D/g,'');

            const country = countryCodes.filter(country => country[0] === Number(countryCodeNumber))[0][1] as any;

            setCountryCodeState((_) => country);
        }).catch(e => {
            const country = countryCodes.filter(country => country[0] === 1)[0][1] as any;
            setCountryCodeState((_) => country);
        });
    }

    function _setFirstUserState(userInfo: userInfoType) {
        setUsernameState((_) => userInfo['username']);
        setEmailState((_) => userInfo['email']);
        setFirstNameState((_) => userInfo['first_name']);
        setSecondNameState((_) => userInfo['second_name']);

        const genre = genres.filter(genre => genre[0] === userInfo['genre']);
        setGenreState((_) => genre.length > 0 ? genre[0][1] as any : genres[0][1]);

        if(userInfo['country_code']) {
            const countryName = countryCodes.filter(country => country[0] === userInfo['country_code']);
            setCountryCodeState((_) => countryName ? countryName[0][1] as any : countryCodes[0][1]);
        }
        else {
            _getGeoInfo();
        }
    }

    function _setFirstColorsState(userInfo: userInfoType) {
        setBackgroundColorState((_) => userInfo['color_configs']['background_color']);
        setMenuColorState((_)  => userInfo['color_configs']['menu_color']);
        setButtonColorState((_) => userInfo['color_configs']['button_color']);
        setTextColorState((_) => userInfo['color_configs']['text_color']);
        setMusicBackgroundColorState((_) => userInfo['color_configs']['music_background_color']);
    }

    useEffect(() => {
        if (userInfoState) {
            _setFirstUserState(userInfoState);

            _setFirstColorsState(userInfoState);
        }
    }, [userInfoState]);

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

    function SaveUserInfo(e: React.FormEvent<HTMLFormElement>): void {
        e.preventDefault();

        if(!jwtTokenState || !userInfoState) {
            return;
        }

        const data = {
            "username": usernameState,
            "first_name": firstNameState ? firstNameState : " ",
            "last_name": secondNameState ? secondNameState : " ",
            "email": emailState,
            "color_configs": {
                "background_color": backgroundColorState,
                "menu_color": menuColorState,
                "button_color": buttonColorState,
                "text_color": textColorState,
                "music_background_color": musicBackgroundColorState
            },
            "other_settings": {
                "genre": genres.filter(genre => genre[1] === genreState)[0][0],
                "country_code": countryCodes.filter(country => country[1] === countryCodeState)[0][0] as Number
            }
        }

        axios.patch('https://fjackson.pythonanywhere.com/user/', data, {
            headers: {
                'token': jwtTokenState
            }
        }).then(response => {
            _setUserInfo();
            _GetToken(response.data);
        }).catch(error => {
            if('token' in error.response.data) {
                const data = error.response.data;
        
                _GetToken(data);
            }
            else {
                _Logout();
            }
        });
    }

    function _setUserInfo() {
        const new_data = {
            "username": usernameState,
            "first_name": firstNameState ? firstNameState : " ",
            "last_name": secondNameState ? secondNameState : " ",
            "email": emailState,
            "genre": genres.filter(genre => genre[1] === genreState)[0][0],
            "country_code": countryCodes.filter(country => country[1] === countryCodeState)[0][0] as Number,
            "color_configs": {
                "background_color": backgroundColorState,
                "menu_color": menuColorState,
                "button_color": buttonColorState,
                "text_color": textColorState,
                "music_background_color": musicBackgroundColorState
            },
        }

        setUserInfoState((_) => new_data as any);
    }

    return (
        <div className={styles.configs__container}>
            <form action="" onSubmit={SaveUserInfo}>
                <div className={styles.user__image__container}>
                    <img 
                        src={process.env.PUBLIC_URL + 'assets/img/user-image.webp'} 
                        alt="Your user" 
                        className={styles.user__image}
                    />
                    <input 
                        type="file" 
                        name="put__image" 
                        id="put__image"
                        accept="image/*"
                        className={styles.put__image}
                        style={inputStyle}
                    />
                    <label 
                        htmlFor="put__image"
                        style={inputStyle}
                    >
                        New picture
                    </label>
                </div>
                <div className={styles.save__button}>
                    <Button 
                        type="submit"
                    >
                        Save
                    </Button>
                </div>
                <div 
                    className={classNames({
                        [styles.inputs__container]: true,
                        [styles.inputs__container__user]: true
                    })}
                >
                    <Input 
                        type="text"
                        name='username'
                        placeholder="Username"
                        value={usernameState}
                        onChange={(e) => setUsernameState(e.currentTarget.value)}
                        pattern={'[a-zA-Z1-9\-]+'}
                    />
                    <Input 
                        type="text"
                        name='email'
                        placeholder="Email"
                        value={emailState}
                        onChange={(e) => setEmailState(e.currentTarget.value)}
                        pattern={'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}
                    />
                    <div className={styles.inputs__container}>
                        <Input 
                            type="text"
                            name='first_name'
                            placeholder="First_Name"
                            value={firstNameState}
                            onChange={(e) => setFirstNameState(e.currentTarget.value)}
                            pattern={`[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð" ',/.-]{0,30}$`}
                        />
                        <Input 
                            type="text"
                            name='second_name'
                            placeholder="Second_Name"
                            value={secondNameState}
                            onChange={(e) => setSecondNameState(e.currentTarget.value)}
                            pattern={`[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð" ',/.-]{0,30}$`}
                        />
                    </div>
                    <div 
                        className={classNames({
                            [styles.inputs__container]: true,
                            [styles.inputs__container__colors]: true
                        })}
                    >
                        <Select
                            name="country_code"
                            options={countryCodes.map(country => country[1] as string)}
                            value={countryCodeState}
                            onChange={(e) => setCountryCodeState(e.currentTarget.value)}
                        />
                        <Select
                            name="genre"
                            options={genres.map(genre => genre[1])}
                            value={genreState}
                            onChange={(e) => setGenreState(e.currentTarget.value)}
                        />
                    </div>
                </div>
                <div className={styles.inputs__container}>
                    <Input 
                        type="color"
                        name="background_color"
                        value={backgroundColorState}
                        onChange={(e) => setBackgroundColorState(e.currentTarget.value)}
                        pattern={'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'}
                    />
                    <Input 
                        type="color"
                        name="menu_color"
                        value={menuColorState}
                        onChange={(e) => setMenuColorState(e.currentTarget.value)}
                        pattern={'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'}
                    />
                    <Input 
                        type="color"
                        name="button_color"
                        value={buttonColorState}
                        onChange={(e) => setButtonColorState(e.currentTarget.value)}
                        pattern={'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'}
                    />
                    <Input 
                        type="color"
                        name="text_color"
                        value={textColorState}
                        onChange={(e) => setTextColorState(e.currentTarget.value)}
                        pattern={'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'}
                    />
                    <Input 
                        type="color"
                        name="music_background_color"
                        value={musicBackgroundColorState}
                        onChange={(e) => setMusicBackgroundColorState(e.currentTarget.value)}
                        pattern={'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'}
                    />
                </div>
            </form>
        </div>
    );
}