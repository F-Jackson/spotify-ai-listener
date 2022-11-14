from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import Http404


def verify_user_auth(request) -> bool:
    if request.user.is_authenticated:
        if request.user.is_anonymous:
            logout(request)
            raise Http404
        return True
    return False


def get_object(request, model) -> object:
    try:
        return model.objects.get(user=request.user)
    except model.DoesNotExist:
        raise Http404


def verify_user_existence(**data) -> object:
    return User.objects.filter(**data)


def verify_serializer(serializer) -> bool:
    return serializer.is_valid()


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
