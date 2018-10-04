from flask_restful import Resource, reqparse, inputs
from flask import jsonify 
from flask_jwt_extended import (create_access_token, jwt_required,
                                create_refresh_token, get_jwt_identity,
                                get_raw_jwt)
from flask_bcrypt import Bcrypt
from ..models.auth import UserModel
from app.jwt import jwt
from ..middleware.middleware import admin_auth, norm_auth

enc = Bcrypt()


class RegisterResource(Resource):

    # get the inputs
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True)

    parser.add_argument('password',
                        type=str,
                        required=True)

    parser.add_argument('email',
                        required=True,
                        help="invalid email",
                        type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))

    def post(self):
        data = RegisterResource.parser.parse_args()
        pas = data['password']
        if len(pas) < 6:
            return {"message": "password must be atleaset six characters "}
        if UserModel(data).get_user_by_email():
            return {"message": "user already registered"}, 400
        else:
            UserModel(data).save()
            return {"message": "user registered"}, 201
        return {"message": "invalid input"}


class LoginResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('email',
                        type=str,
                        required=True)

    parser.add_argument('password',
                        required=True,
                        help="invalid email",
                        type=str)

    def post(self):
        data = LoginResource.parser.parse_args()
        user = UserModel(data).get_user_by_email()
        user_id = user[0]['user_id']
        role = user[0]['role']
        if user:
            if enc.check_password_hash(user[0].get('password'), data['password']):
                access_token = create_access_token(identity=(user_id, role))
                refresh_token = create_refresh_token(identity=(user_id, role))
                return {"message": "user logged in", "access_token":
                        access_token}, 201
        return {"message": "username and password do not match"}, 400


class LogoutResource(Resource):
    @norm_auth
    def post(self):
        jti = get_raw_jwt()['jti']
        token = {'token_blacked': jti}
        blacklisted = UserModel(token).blacklist()
        if blacklisted:
            return {"message": "logged out"}, 200
