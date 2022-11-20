
interface Props {
    type: string,
    name: string,
    placeholder: string
}


export default function Input(props: Props) {
    return (
        <div>
            <label 
                htmlFor={props.name}
            >
                {props.name}
    </label>

            <input 
                type={props.type} 
                name={props.name}
                placeholder={props.placeholder} 
            />
        </div>
    );
}
