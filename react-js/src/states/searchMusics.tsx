import { atom } from "recoil";
import { TMusics } from "types/musicsType";


export const searchMusicsAtom = atom({
    key: "searchMusics",
    default: [] as TMusics[]
});