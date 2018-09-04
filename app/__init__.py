from flask_restful import Api
from flask import Flask 
from instance.config import app_config 


def create_app(config_name): 
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    api = Api(app, prefix='/api/v1')

    return app