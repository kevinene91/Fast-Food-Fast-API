
from flask_restful import Api
from flask import Flask 
from flask_jwt_extended import JWTManager
import os
from instance.config import app_config 

from .api.v1.Landing.views import landing_page
# import resources
from .api.v1.resources.orders import (OrderListResource, OrderResource)
from .api.v1.resources.foods import (FoodListResource, FoodResource, ChangePriceResource)
from .api.v1.resources.auth import RegisterResource, LoginResource, LogoutResource

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

    jwt = JWTManager(app)

    api = Api(app, prefix='/api/v1')

    #register the endpoints
    app.register_blueprint(landing_page)
    api.add_resource(OrderListResource, '/orders')
    api.add_resource(OrderResource, '/orders/<int:id>')
    api.add_resource(FoodListResource, '/foods')
    api.add_resource(FoodResource, '/foods/<int:id>')
    api.add_resource(ChangePriceResource, '/foods/<string:name>')
    api.add_resource(RegisterResource, '/register')
    api.add_resource(LoginResource, '/login')
    api.add_resource(LogoutResource,'/logout')
    return app