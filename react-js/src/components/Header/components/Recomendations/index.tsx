import { useEffect, useState } from 'react';
import { useRecoilValue } from 'recoil';
import { userInfoAtom } from 'states/user';
import { TMusics } from 'types/musicsType';
import Musics from './components/musics';
import styles from './Recomendations.module.scss';


interface Props {
    musics: TMusics[] | undefined
}

export default function Recomendations(props: Props) {
    const userInfoState = useRecoilValue(userInfoAtom);
    const [sliderPositionXState, setSliderPositionXState] = useState(0);
    const [loadedState, setLoadedState] = useState(false);
    const [sliderStyleState, setSliderStyleState] = useState<React.CSSProperties>({
        transform: `translateX(-${sliderPositionXState}px)`
    });

    let recomendationStyle = userInfoState['username'] ? {
        borderColor: userInfoState['color_configs']['button_color']
    } as React.CSSProperties : {} as React.CSSProperties;

    function _MoveSlider() {
        let newPosX: number;
        if(sliderPositionXState / 184 < 29) {
            newPosX = sliderPositionXState + 184;
        }
        else {
            newPosX = 0;
        }
        const newSlider = {
            transform: `translateX(-${newPosX}px)`
        }
        setSliderStyleState((_) => newSlider);
        setTimeout(() => {
            setSliderPositionXState(newPosX);
            _MoveSlider();
        }, 2000);
    }

    useEffect(() => {
        if(!loadedState) {
            setLoadedState(true);
            setTimeout(() => {
                _MoveSlider();
            }, 2000);
        }
    }, []);


    return (
        <div
            className={styles.recomendations}
            style={recomendationStyle}
        >
            <ul
                className={styles.slider}
                style={sliderStyleState}
            >
                {
                    props.musics?.map(music => (
                        <li
                            key={music.id}
                        >
                            <Musics
                                name={music.name}
                                track_id={music.track_id}
                            />
                        </li>
                    ))
                }
            </ul>
        </div>
    );
}