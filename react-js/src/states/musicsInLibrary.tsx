import { atom } from "recoil";
import { TMusics } from "types/musicsType";

export const musicsInLibraryAtom = atom({
    key: "musicsInLibrary",
    default: [] as TMusics[]
});