from flask import request
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required


#local imports
from ..models.auth_models import user_model

class RegisterResource(Resource):
    
    #get the inputs
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True)

    parser.add_argument('password',
    type = str,
    required = True)

    parser.add_argument('email',
    type = str,
    required = True)

    parser.add_argument('address',
    type = str,
    required = True)

    #post data
    def post(self):
        data = RegisterResource.parser.parse_args()
        inc_id = user_model.get_length(user_model.get_all_users()) + 1
        #check if usermail already used
        if user_model.get_by_email(data['email'],user_model.get_all_users()):
            return {"message":"a user registered by that name is already registered"}

        user = {
            "id":inc_id, "username":data["username"], "password":data['password'],
            "email":data['email'], "address":data["address"]
            
        }
        #append to list
        user_model.add_user(user)
        return user

class LoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True)

    parser.add_argument('password',
    type = str,
    required = True)

    def post(self):
        data = LoginResource.parser.parse_args()
        user = user_model.get_by_name(data['username'], user_model.get_all_users())
        
        if user and safe_str_cmp(user['password'], data['password']):
            access_token = create_access_token(identity=user)
            if user_model.get_token(access_token,user_model.get_all_tokens()):
                return {'message': "user token has expired"}
            return {"access_token":access_token}
        elif user_model.get_length(user_model.get_all_users()) == 0:
            return {"message":"please register"}    
        return {"message":"invalid credentials"}, 401

class LogoutResource(Resource):
    @jwt_required
    def post(self):
        token = request.headers.get('Authorization')
        user_model.add_to_black_list({'token':token})
        get_token = user_model.get_token(token,user_model.get_all_tokens())
        if get_token:   
            return {'message':'user has been logged out'}
        return {'message':'invalid token'},401
