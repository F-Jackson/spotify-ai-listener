from account.models import UserStaticsModel, ColorConfigsModel, UserModel

INFO_NOT_GET_USER = (
    'id',
    'user'
)

INFO_MODELS_TO_GET = (
    UserModel,
    ("color_configs", ColorConfigsModel),
    ("statics", UserStaticsModel)
)

NEW_USER_NEEDS = (
    'username',
    'email',
    'password'
)

LOGIN_USER_NEED = (
    'username',
    'password'
)

INFO_TO_DELETE_USER = (
    'password'
)

USER_UPDATE_NEED = (
    "username",
    "first_name",
    "last_name",
    "email",
    {
        "color_configs": [
            "background_color",
            "menu_color",
            "button_color",
            "text_color",
            "music_background_color"
        ],
        "other_settings": [
            "genre",
            "country_code"
        ]
    }
)
