
from flask_restful import Api
from flask import Flask 
from instance.config import app_config 

# import resources
from app.resources.orders import OrderListResource

def create_app(config_name): 
    """
        creates the app and registers the endpoints
    """
    #initialize flas
    app = Flask(__name__, instance_relative_config=True) 
    # add configs
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    #add the prefix
    api = Api(app, prefix='/api/v1')

    #register the endpoints
    api.add_resource(OrderListResource, '/orders')
    return app