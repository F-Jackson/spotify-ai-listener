import Button from 'components/Button';
import { useRecoilValue } from 'recoil';
import { userInfoAtom } from 'states/user';
import styles from './Musics.module.scss';


interface Props {
    name: string,
    genre: string,
    track_id: string
}

export default function Musics(props: Props) {
    const userInfoState = useRecoilValue(userInfoAtom);
    
    let musicStyle = userInfoState['username'] ? {
        backgroundColor: userInfoState['color_configs']['music_background_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    let textStyle = userInfoState['username'] ? {
        textColor: userInfoState['color_configs']['text_color']
    }  as React.CSSProperties : {} as React.CSSProperties;

    return (
        <article
            className={styles.music}
            style={musicStyle}
        >
            <img 
                src={process.env.PUBLIC_URL + '../assets/img/music-image.webp'} 
                alt="music"
                className={styles.music_image}
            />
            <p
                className={styles.music__title}
                style={textStyle}
            >
                {props.name}
            </p>
            <p
                className={styles.music__genre}
                style={textStyle}
            >
                {props.genre}
            </p>
            <Button
                onClick={() => window.open(`https://open.spotify.com/track/${props.track_id}`)}
            >
                Listen
            </Button>
        </article>
    );
}