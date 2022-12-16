import { Link } from "react-router-dom";
import { useRecoilValue } from "recoil";
import { userInfoAtom } from "states/user";
import styles from "./NavButton.module.scss";


interface Props {
    link: string,
    text: string,
    children: React.ReactNode | JSX.Element,
}

export default function NavButton(props: Props) {
    const userInfoState = useRecoilValue(userInfoAtom);

    let buttonStyle = userInfoState['username'] ? {
        backgroundColor: userInfoState['color_configs']['button_color'],
        textColor: userInfoState['color_configs']['text_color']
    } as React.CSSProperties : {} as React.CSSProperties;

    let nameStyle = userInfoState['username'] ? {
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;


    return (
        <Link 
            to={props.link}
            className={styles.link}
            style={buttonStyle}
        >
            <span
                style={nameStyle}
            >
                {props.text}
            </span> 
            {props.children}
        </Link>
    );
}
