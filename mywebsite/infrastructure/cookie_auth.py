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