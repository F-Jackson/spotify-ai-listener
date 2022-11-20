import classNames from 'classnames';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import styles from "./Header.module.scss";

import { SiApplemusic } from "react-icons/si";
import { MdLibraryMusic } from "react-icons/md";
import { RiMenuFoldFill, RiMenuLine } from "react-icons/ri";


export default function Header() {
    const [menuActive, useMenuActive] = useState(false)

    function ActiveMenu() {
        useMenuActive(!menuActive)
    }

    return (
        <header className={classNames({
            [styles.header]: true,
            [styles["header-desactive"]]: !menuActive
        })}>
            <RiMenuFoldFill 
                className={classNames({
                    [styles.hambuger__button]: true,
                    [styles['hambuger__button-desative']]: !menuActive
                })} 
                onClick={() => ActiveMenu()} 
            />
            <RiMenuLine 
                className={classNames({
                    [styles.hambuger__button]: true,
                    [styles['hambuger__button-active']]: menuActive
                })} 
                onClick={() => ActiveMenu()} 
            />
            <div className={styles.user}>
                <img src="" alt=""/>
                <div className={styles.user__info}>
                    <p>name rokerok jdhsfgkdsjks</p>
                    <Link to="#"></Link>
                </div>
            </div>
            <nav className={styles.links}> 
                <Link to="#" className={styles.link}>
                    <span>Listen Music</span> 
                    <SiApplemusic className={styles.icon}/> 
                </Link>
                <Link to="#" className={styles.link}>
                    <span>My Librarys</span> 
                    <MdLibraryMusic className={styles.icon}/> 
                </Link>
            </nav>
            <section className={styles.recomendations}></section>
        </header>
    );
}