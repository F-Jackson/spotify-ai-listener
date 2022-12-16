import { atom } from "recoil";

export const userInfoAtom = atom({
    key: 'userInfo',
    default: {
        'username': "",
        'email': "",
        'first_name': "",
        'second_name': "",
        'genre': "",
        'country_code': "",
        'color_configs': {
            'background_color': "",
            'menu_color': "",
            'button_color': "",
            'text_color': "",
            'music_background_color': ""
        }
    }
})