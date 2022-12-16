from user.constants._views import NEW_USER_NEEDS, USER_UPDATE_NEED, LOGIN_USER_NEED, INFO_TO_DELETE_USER

USER = {
    'url': '/user',
    'methods': [
        {
            'method': 'get',
            'info': 'Get user info if user is logged or 404'
        },
        {
            'method': 'post',
            'info': 'Sign in user',
            'request template': LOGIN_USER_NEED
        },
        {
            'method': 'put',
            'info': 'Create user if user inst logged',
            'request template': NEW_USER_NEEDS
        },
        {
            'method': 'patch',
            'info': 'Update user if user is logged',
            'request template': USER_UPDATE_NEED
        },
        {
            'method': 'delete',
            'info': 'Delete user if is logged',
            'request template': INFO_TO_DELETE_USER
        },
    ]
}

DOCS = [
    USER
]
