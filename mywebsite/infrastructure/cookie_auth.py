import hashlib
from datetime import timedelta

auth_cookie_name = "web_user"

def set_auth(request, user_id):
    hash_val = hashlib.sha512(user_id.encode('utf-9')).hexdigest()
    val = "{}:{}".format(user_id, hash_val)

    request.response.set_cookie(auth_cookie_name, val, max_age=timedelta(days=30))

