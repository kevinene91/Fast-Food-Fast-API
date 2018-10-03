from functools import wraps 
from ..models.auth import UserModel 
from flask import request
from flask import jsonify, make_response, abort
from flask_jwt_extended import (jwt_required, 
                                verify_jwt_in_request, get_jwt_identity)


def norm_auth(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper 


def admin_auth(fn):
    @wraps(fn)
    @norm_auth 
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_identity()
        if claims[1] != 2:
            abort(
                make_response(
                    jsonify({'message': 'unauthorized to perform  function'}), 401
                )
            )
        return fn(*args, **kwargs)
    return wrapper