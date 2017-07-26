import hashlib
from datetime import timedelta

auth_cookie_name = "kkoivu_user"

def set_auth(request, user_id):
    hash_val = hashlib.sha512(user_id.encode('utf-8')).hexdigest()
    val = "{}:{}".format(user_id, hash_val)

    request.response.set_cookie(auth_cookie_name, val, max_age=timedelta(days=30))
    request.add_response_callback(lambda request, response: __add_cookie_callback(request, response, auth_cookie_name, val))

def __add_cookie_callback(_, response, name, value):
    response.set_cookie(name, value, max_age=timedelta(days=30))

def get_user_id_from_cookie(request):
    if auth_cookie_name not in request.cookies:
        return None

    val = request.cookies[auth_cookie_name]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    user_id = parts [0]
    hash_val = parts[1]
    hash_val_check = hashlib.sha512(user_id.encode('utf-8')).hexdigest()
    if hash_val != hash_val_check:
        print("Hash mismatch, invalid cookie")
        return None

    return user_id