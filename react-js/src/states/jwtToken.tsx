import { atom } from "recoil";

export const jwtTokenAtom = atom({
    key: 'jwtToken',
    default: ""
});
