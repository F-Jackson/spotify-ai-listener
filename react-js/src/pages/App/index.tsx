
import Header from "components/Header";

import styles from "./App.module.scss";
import { Outlet } from "react-router-dom";

export default function App() {
    return(
        <>
            <Header />
            <main className={styles.main}>
                <Outlet/>
            </main>
        </>
    );
}