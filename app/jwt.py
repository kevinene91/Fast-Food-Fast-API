from flask_jwt_extended import JWTManager
jwt = JWTManager()
from .api.v2.models.auth import UserModel


@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token['jti']
    token = {'token_blacked': jti}
    mycheck = UserModel(token).check_if_blacklist()
    return not mycheck
