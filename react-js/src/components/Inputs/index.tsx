import { FormEvent } from "react";
import { useRecoilValue } from "recoil";
import { userInfoAtom } from "states/user";
import styles from "./Inputs.module.scss";

interface Props {
    type: string,
    name: string,
    placeholder?: string,
    value?: string,
    onChange?: (e: FormEvent<HTMLInputElement>) => void
    pattern?: string
}


export default function Input(props: Props) {
    const userInfoState = useRecoilValue(userInfoAtom);

    let inputStyle = userInfoState ? {
        borderColor: userInfoState['color_configs']['button_color'],
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let labelStyle = userInfoState ? {
        backgroundColor: userInfoState['color_configs']['menu_color'],
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;


    return (
        <div className={styles.container}>
            <label 
                htmlFor={props.name}
                className={styles.label}
                style={labelStyle}
            >
                {props.name}
            </label>

            <input 
                type={props.type} 
                name={props.name}
                placeholder={props.placeholder}
                id={props.name}
                className={styles.input}
                value={props.value}
                onChange={props.onChange}
                pattern={props.pattern}
                style={inputStyle}
            />
        </div>
    );
}
