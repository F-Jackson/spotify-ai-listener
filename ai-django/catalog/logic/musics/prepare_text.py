from textblob import TextBlob
from unidecode import unidecode

from catalog.constants._prepare_text import STOP_WORDS


def correct_text(text: str) -> str:
    return TextBlob(text).words


def lower_word(word: str) -> str:
    return word.lower()


def remove_stop_words(word: str) -> str | None:
    if word in STOP_WORDS:
        return word


def strip_word(word: str) -> str:
    return word.strip(" .,:><~^´`'!@#$%¨&*()_-=+[]{}ªº§;|?/*₢")


def convert_to_unicode(word: str) -> str:
    return unidecode(word)


STEPS_TO_PREPARE_TEXT = (
    lower_word,
    remove_stop_words,
    strip_word,
    convert_to_unicode
)


def prepare_text(text: str) -> list[str]:
    corrected_text = correct_text(text)

    words = []

    for word in corrected_text:
        new_word = word
        for step in STEPS_TO_PREPARE_TEXT:
            if step(new_word):
                new_word = step(new_word)
        words.append(new_word)

    return words
