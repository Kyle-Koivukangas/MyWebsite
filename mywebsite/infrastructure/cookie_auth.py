import hashlib
from datetime import timedelta

auth_cookie_name = "kkoivu_user"

def set_auth(request, user_id):
    hash_val = __hash_text(user_id)
    val = "{}:{}".format(user_id, hash_val)

    request.response.set_cookie(auth_cookie_name, val, max_age=timedelta(days=30))
    request.add_response_callback(lambda request, response: __add_cookie_callback(request, response, auth_cookie_name, val))

def __add_cookie_callback(_, response, name, value):
    response.set_cookie(name, value, max_age=timedelta(days=30))

def get_user_id_from_cookie(request):
    if auth_cookie_name not in request.cookies:
        return None

    cookie_value = request.cookies[auth_cookie_name]
    parts = cookie_value.split(':')
    if len(parts) != 2:
        return None

    user_id = parts[0]
    expected_hash = parts[1]
    hash_val = __hash_text(user_id)
    if hash_val != expected_hash:
        print("Hash mismatch, invalid cookie")
        return None

    return user_id

def __hash_text(text):
    text = "my_saltshake_brings" + text + "all_the_boys_to_the_yard"
    return hashlib.sha512(text.encode('utf-8')).hexdigest()

def logout(request):
    request.add_response_callback(lambda request, response: __clear_cookie_callback(response, auth_cookie_name))


def __clear_cookie_callback(response, name):
    response.delete_cookie(name)
