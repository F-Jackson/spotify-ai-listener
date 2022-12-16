from catalog.constants._validators import LIBRARY_MAX_SIZE
from catalog.validators.serializer_validation import SerializerValidator


def validate_photo(photo):
    validators = [
        (photo.size <= LIBRARY_MAX_SIZE, f'Image size must have {LIBRARY_MAX_SIZE} or less')
    ]

    return SerializerValidator.validate(validators)
