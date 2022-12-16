import { ReactNode } from 'react';
import { useRecoilValue } from 'recoil';
import { userInfoAtom } from 'states/user';
import uniqid from 'uniqid';
import styles from "./Select.module.scss";

interface Props {
    name: string,
    options: string[],
    value: string,
    onChange: React.ChangeEventHandler<HTMLSelectElement>
}

export default function Select(props: Props) {
    const userInfoState = useRecoilValue(userInfoAtom);

    let selectStyle = userInfoState ? {
        borderColor: userInfoState['color_configs']['button_color'],
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    function handleOptions(options: string[]): ReactNode {
        return options?.map((option) => {

            return <option
                        value={option ?  option : "None"}
                        key={uniqid()}
                    >
                        {option ? option : "None"}
                    </option>
        });
    }

    return (
        <div 
            className={styles.container}
        >
            <label 
                htmlFor={props.name}
                className={styles.label}

            >
                {props.name}
            </label>
            <select
                name={props.name}
                id={props.name}
                className={styles.select}
                value={props.value}
                onChange={props.onChange}
                title={props.name}
                style={selectStyle}
            >
                {handleOptions(props.options)}
            </select>
        </div>
    );
}