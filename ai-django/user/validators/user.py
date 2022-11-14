from user.constants._validators import USER_USERNAME_MAX_SIZE, USER_USERNAME_REGEX, USER_PASSWORD_REGEX, \
    USER_NAME_REGEX, USER_LAST_LOGIN_REGEX
from user.validators.common import valide_max_length, valide_regex
from user.validators.serializer_validation import SerializerValidator
from validate_email import validate_email as email_is_valid


def validate_username(username):
    validators = [
        (valide_max_length(len(username), USER_USERNAME_MAX_SIZE),
            f'username length must less than {USER_USERNAME_MAX_SIZE}'),
        (valide_regex(username, USER_USERNAME_REGEX),
            f'username doesnt match the pattern: {USER_USERNAME_REGEX}')
    ]

    return SerializerValidator.validate(validators)


def validate_password(password):
    validators = [
        (valide_regex(password, USER_PASSWORD_REGEX),
            'The password must contain minimum of eight characters, at least one letter, one number and one special '
            'character')
    ]

    return SerializerValidator.validate(validators)


def validate_names(name):
    validators = [
        (valide_regex(name, USER_NAME_REGEX),
            'The size must be: between 2 and 70; '
            'Must contains only: a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊ'
            'ËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.-')
    ]

    return SerializerValidator.validate(validators)


def validate_email(email):
    validators = [
        # (email_is_valid(email),
        #  'Insert a valid Email')
    ]

    return SerializerValidator.validate(validators)
