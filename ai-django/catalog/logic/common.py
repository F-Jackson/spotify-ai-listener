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
