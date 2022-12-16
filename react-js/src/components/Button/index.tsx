import React from "react";
import { useRecoilValue } from "recoil";
import styles from "./Button.module.scss";
import { userInfoAtom } from 'states/user';

interface Props {
    onClick?: () => void,
    children?: React.ReactNode | JSX.Element,
    type?: "button" | "submit" | "reset" | undefined
}


export default function Button(props: Props) {
    const userInfoState = useRecoilValue(userInfoAtom);

    let buttonStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['button_color'],
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    return (
        <button
            type={props.type}
            onClick={props.onClick}
            className={styles.button}
            style={buttonStyle}
        >
            {props.children}
        </button>
    );
}