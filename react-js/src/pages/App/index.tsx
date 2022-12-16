
import Header from "components/Header";

import styles from "./App.module.scss";
import { Outlet } from "react-router-dom";
import { CookiesProvider } from "react-cookie";
import { userInfoAtom } from "states/user";
import { useRecoilValue } from "recoil";

export default function App() {
    const userInfoState = useRecoilValue(userInfoAtom);

    let mainStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['background_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    return(
        <CookiesProvider>
            <Header />
            <main 
                className={styles.main}
                style={mainStyle}
            >
                <Outlet/>
            </main>
        </CookiesProvider>
    );
}