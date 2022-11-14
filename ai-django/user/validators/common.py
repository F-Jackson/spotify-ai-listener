import re


def valide_max_length(value, max_size) -> bool:
    return value <= max_size


def valide_regex(value: str, regex: str) -> bool:
    pattern = re.compile(regex)
    return pattern.fullmatch(value) is not None
