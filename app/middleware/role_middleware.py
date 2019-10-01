from functools import wraps
from flask import request

from app.helpers.auth_helper import Auth
from app.helpers.response_helper import ResponseHelper


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data = Auth.get_user(request)
        meta_error = data.get('meta')['error']
        if meta_error:
            meta_msg = data.get('meta')['message']
            return ResponseHelper.error_custom(401, meta_msg)
        return f(*args, **kwargs)
    return decorated


def admin_token_required(levels=[]):
    def decoration(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            data = Auth.get_user(request)
            meta_error = data.get('meta')['error']
            if meta_error:
                meta_msg = data.get('meta')['message']
                return ResponseHelper.error_custom(401, meta_msg)

            level_name = data.get('data')['level']['name']
            if level_name not in levels:
                return ResponseHelper.error_custom(401, 'admin token required')

            return f(*args, **kwargs)
        return decorated
    return decoration
