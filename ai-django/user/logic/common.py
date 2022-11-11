from django.contrib.auth.models import User
from django.http import Http404


def get_object(request, model) -> object:
    try:
        return model.objects.get(user=request.user)
    except model.DoesNotExist:
        raise Http404


def verify_user_existence(**data) -> bool:
    return User.objects.filter(**data) is not None


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
            print(atr, data.keys())
            v.append(atr in data.keys())
    return all(v)
