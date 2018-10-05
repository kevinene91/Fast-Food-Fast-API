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
                        required=True,
                        type=str
                        )

    parser.add_argument('password',
                        help=" invalid password atleast 6 characters no spaces",
                        type=str,
                        required=True)

    parser.add_argument('email',
                        required=True,
                        help="invalid email",
                        type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))

    parser.add_argument('role',
                        required=True,
                        type=int)

    def post(self):
        data = RegisterResource.parser.parse_args()
        username = data['username']
        fixed_space = ''.join(username.split())
        myinputs = [data['password'], fixed_space]
        expected = [1, 2]
        data['username'] = fixed_space
        thevalue = None
        #username and password should be atleast six character
        for i in range(len(myinputs)):
            if len(myinputs[i]) < 6:
                value_name = myinputs[i]
                thevalue = [key for (key, value) in data.items()
                            if value == value_name]
                length_update_message = "{} should be atleast six characters".format(thevalue[0])
                return {"message": length_update_message}
        if data['role'] in expected: 
            if UserModel(data).get_user_by_email():
                return {"message": "user already registered"}, 400
            else:
                UserModel(data).save()
                if data['role'] == 2:
                    return {"message": "admin user registered"}, 201
                return {"message": "user registered "}, 201
            return {"message": "invalid input"}
        return {"message": "only admin or normal user roles"}


class LoginResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('email',
                        type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
                        help="invalid email input",
                        required=True)

    parser.add_argument('password',
                        required=True,
                        help="invalid password",
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


class UsersResource(Resource):

    @admin_auth
    def get(self):
        data = {"table": "users"}
        mylist = UserModel(data).get_all()
        return jsonify(mylist)
