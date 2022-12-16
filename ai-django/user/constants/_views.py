from account.models import UserStaticsModel, ColorConfigsModel, UserModel
from account.serializers import OtherSettingsSerializer, ColorConfigsSerializer, UserStaticsSerializer


INFO_MODELS_TO_GET = (
    {'model': UserModel, 'serializer': OtherSettingsSerializer},
    {'name': "color_configs", 'model': ColorConfigsModel, 'serializer': ColorConfigsSerializer},
    {'name': "statics", 'model': UserStaticsModel, 'serializer': UserStaticsSerializer}
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
    'username',
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
