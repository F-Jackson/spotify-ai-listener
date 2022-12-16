from django.contrib.auth.models import User
from django.http import Http404

from jwt_auth.logic.verify_client_token import ClientTokenVerifier


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


def get_object(user: User, model) -> object:
    try:
        return model.objects.get(user=user)
    except model.DoesNotExist:
        raise Http404


def verify_user_existence(**data) -> object:
    return User.objects.filter(**data)


def request_keys_verifier(data, verifier):
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


def dont_has_email(user: User, email: str) -> bool:
    user_email = getattr(user, 'email')

    if user_email != email:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return True
        else:
            return False
    return True
