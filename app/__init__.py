import os
from flask_restful import Api
from flask import Flask 
from flask_jwt_extended import JWTManager
from .jwt import jwt
from instance.config import app_config 
from .api.v2.db.conn import create_db
from .api.v2 import apiv2
from .api.v1 import apiv1

from app.bcrypt import BCRYPT


def create_app(config_name): 
    """
        creates the app and registers the endpoints
    """
    # initialize flask
    app = Flask(__name__, instance_relative_config=True)
    # add configs
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    BCRYPT.init_app(app)
    jwt.init_app(app)
    # add the prefix
    with app.app_context():
        create_db()

    app.register_blueprint(apiv2)    
    app.register_blueprint(apiv1)
    return app