
from flask_restful import Api
from flask import Flask 
from flask_jwt_extended import JWTManager
import os
from instance.config import app_config 

from .api.v2.db.conn import create_db

# import resources
from .api.v2.resources.orders import (OrdersListResource, OrdersResource, UsersOrdersResource)
from .api.v2.resources.meals import (FoodListResource, FoodResource)
from .api.v2.resources.auth import (RegisterResource, LoginResource)
from .api.v2.resources.menu_items import (MenuItemResource, MenuItemListResource)
from .api.v2.resources.menu import (MenuListResource, MenuResource)

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
    create_db()
    jwt = JWTManager(app)


    api2 = Api(app, prefix='/api/v2')

    #register v1 endpoints

    #register v2 endpointscl
    api2.add_resource(RegisterResource, '/auth/signup')
    api2.add_resource(LoginResource, '/auth/login')
    api2.add_resource(UsersOrdersResource, '/user/orders')
    api2.add_resource(OrdersListResource, '/orders')
    api2.add_resource(OrdersResource, '/orders/<int:id>')
    api2.add_resource(MenuListResource, '/menu')
    api2.add_resource(MenuResource, '/menu/<int:id>')
    api2.add_resource(FoodListResource, '/meals')
    api2.add_resource(FoodResource, '/meals/<int:id>')
    api2.add_resource(MenuItemResource, '/menuitem/<int:id>')
    api2.add_resource(MenuItemListResource, '/menuitem')

    # api2.add_resource(LogoutResource,'/logout')
    return app