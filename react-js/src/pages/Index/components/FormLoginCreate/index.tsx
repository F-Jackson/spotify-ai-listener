import styles from "./FormLoginCreate.module.scss";
import Button from "components/Button";
import Input from "components/Inputs";
import axios from "axios";
import { useState } from "react";
import { jwtTokenAtom } from "states/jwtToken";
import { useRecoilState, useSetRecoilState } from "recoil";
import { useCookies } from "react-cookie";
import { resetUserInfo } from "utils/_resetUserInfo";
import { userInfoAtom } from "states/user";
import { librarysAtom } from "states/librarys";
import { useNavigate } from "react-router-dom";


interface Props {
    loginOrCreate: "login" | "create",
}

type requestStatus = 'failed' | 'sucess' | 'send';

export default function FormLoginCreate(props: Props){
    const [usernameState, setUsernameState] = useState('');
    const [emailState, setEmailState] = useState('');
    const [passwordState, setPasswordState] = useState('');

    const [requestStatusState, setRequestStatusState] = useState<requestStatus>('send');

    const [tokenState, setJwtTokenState] = useRecoilState(jwtTokenAtom);
    const setLibrarysState = useSetRecoilState(librarysAtom);
    const setUserInfoState = useSetRecoilState(userInfoAtom);
    
    const [cookies, setCookie, removeCookie] = useCookies(['token']);

    const navigate = useNavigate();
    

    function _requestFail() {
        setRequestStatusState((_) => 'failed');
        _Logout();
    }

    function _Logout() {
        setLibrarysState((_) => []);
        setUserInfoState((_) => resetUserInfo());
        setJwtTokenState((_) => "");
        removeCookie('token', { path: '/'});
        navigate("/");
    }

    function _GetToken(data: any) {
        const token: string = data['token'];
    
        setJwtTokenState((_) => token);
        setCookie('token', token, { path: '/' });
    }

    function CreateUser(e: any) {
        e.preventDefault();
        axios.put('https://fjackson.pythonanywhere.com/user/', {
            username: usernameState,
            email: emailState,
            password: passwordState
        }).then((response) => {
            setRequestStatusState((_) => 'sucess');
            _Logout();
        }).catch((error) => {
            _requestFail();
        });
    }

    function LoginUser(e: any) {
        e.preventDefault();
        axios.post('https://fjackson.pythonanywhere.com/user/', {
            username: usernameState, 
            password: passwordState
        }, {
            headers: {
                'token': tokenState
            }
        }).then((response) => {
            if('token' in response.data){
                _GetToken(response.data);
                setRequestStatusState((_) => 'sucess');
            }
            else { 
                _requestFail();
            }
        }).catch((error) => {
            _requestFail();
        });
    }


    return (
        <form 
            className={styles.form__container}
            onSubmit={props.loginOrCreate === "create" ? CreateUser : LoginUser}
        >
            <Input
                name="username"
                placeholder="Username"
                type="text"
                value={usernameState}
                onChange={(e) => setUsernameState(e.currentTarget.value)}
            />
            {
                props.loginOrCreate === "create" &&
                <Input
                    name="email"
                    placeholder="Email"
                    type="text"
                    value={emailState}
                    onChange={(e) => setEmailState(e.currentTarget.value)}
                />
            }
            <Input
                name="password"
                placeholder="Password"
                type="text"
                value={passwordState}
                onChange={(e) => setPasswordState(e.currentTarget.value)}
            />
            <Button 
                type="submit"
            >
                {props.loginOrCreate === 'create' ? 'create' : 'login'}
            </Button>
        </form>
    );
}