import { HiPlayPause } from "react-icons/hi2";
import styles from './Musics.module.scss';
import { userInfoAtom } from "states/user";
import { useRecoilValue } from "recoil";
import Button from "components/Button";

interface Props {
    name: string,
    track_id: string
}

export default function Musics(props: Props) {
    const userInfoState = useRecoilValue(userInfoAtom);

    let musicsStyle = userInfoState['username'] ? {
        backgroundColor: userInfoState['color_configs']['music_background_color']
    } as React.CSSProperties : {} as React.CSSProperties;

    let titleStyle = userInfoState['username'] ? {
        color: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let iconStyle = userInfoState['username'] ? {
        color: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;


    return (
        <article
            className={styles.musics}
            style={musicsStyle}
        >
            <p
                className={styles.title}
                style={titleStyle}
            >
                {props.name}
            </p>
            <Button 
                onClick={() => window.open(`https://open.spotify.com/track/${props.track_id}`)}
            >
                <HiPlayPause style={iconStyle}/>
            </Button>
        </article>
    );
}