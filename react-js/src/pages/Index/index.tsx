import Button from "components/Button";
import styles from "./Index.module.scss";
import { useState } from "react";
import FormLoginCreate from "./components/FormLoginCreate";
import { useRecoilState } from "recoil";
import { jwtTokenAtom } from "states/jwtToken";
import Recomendations from "./components/Recomendations";


type accountFunctions = "login" | "create"


export default function Index() {
    const [loginOrCreate, setLoginOrCreate] = useState<accountFunctions>("login");

    const [jwtTokenState, setJwtTokenState] =  useRecoilState(jwtTokenAtom);

    function changeAccountFunction() {
        if (loginOrCreate === "login") {
            setLoginOrCreate("create")
        }
        else {
            setLoginOrCreate("login")
        }
    }

    return (
        <div className={styles.index__container}>
            <section className={styles.image__container}>
                <img 
                    src={process.env.PUBLIC_URL + 'assets/img/spotify.png'} 
                    alt="Spotify Logo"
                />
            </section>
            <section className={styles.account__container}>
                {
                    !jwtTokenState ? 
                    <>
                        <div className={styles.account__sign}>
                            <Button onClick={() => changeAccountFunction()}>
                                {loginOrCreate === "login" ? "sign in" : "sign up"}
                            </Button>
                        </div>
                        <FormLoginCreate
                            loginOrCreate={loginOrCreate}
                        />
                    </>
                    :
                    <Recomendations />
                }
            </section>
        </div>
    );
}