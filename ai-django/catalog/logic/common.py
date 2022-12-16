from django.contrib.auth.models import User

from jwt_auth.logic.verify_client_token import ClientTokenVerifier


def request_keys_verifier(data: dict, verifier: tuple):
    v = []
    for atr in verifier:
        if type(atr) == dict:
            for key, value in atr.items():
                if str(key) in data.keys():
                    v.append(request_keys_verifier(data[str(key)], value))
                else:
                    v.append(False)
        else:
            v.append(atr in data.keys())

    return all(v)


def request_keys_filter(data: dict, verifier: tuple) -> dict:
    new_data = {}
    for key, value in data.items():
        if key in verifier:
            new_data[key] = value

    return new_data


def verify_user_auth(request, get_user: bool = False) -> None | dict[str, str]:
    token = str(request.META.get('HTTP_TOKEN'))
    if token:
        jwt = ClientTokenVerifier(token)
        jwt_is_valid = jwt.valid_client_token()
        if jwt_is_valid:
            token = jwt.client_token[0]
            user_id = jwt.client_token[1]['sub']

            data = {
                'token': token,
                'user_id': user_id
            }

            if get_user:
                try:
                    user = User.objects.get(pk=user_id)
                except User.DoesNotExist:
                    return None
                else:
                    data.update({'user': user})

            return data
    return None
