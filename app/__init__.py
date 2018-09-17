
from flask_restful import Api
from flask import Flask 
from instance.config import app_config 

# import resources
from .api.v1.resources.orders import (OrderListResource, OrderResource)
from .api.v1.resources.foods import (FoodListResource, FoodResource)

def create_app(config_name): 
    """
        creates the app and registers the endpoints
    """
    #initialize flask
    app = Flask(__name__, instance_relative_config=True) 
    # add configs
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    #add the prefix
    api = Api(app, prefix='/api/v1')

    #register the endpoints
    api.add_resource(OrderListResource, '/orders')
    api.add_resource(OrderResource, '/orders/<int:id>')
    api.add_resource(FoodListResource, '/foods')
    api.add_resource(FoodResource, '/foods/<int:id>')
    return app