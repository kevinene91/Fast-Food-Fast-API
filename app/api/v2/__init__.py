from flask import Blueprint
from flask_restful import Api

from .resources.orders import (CustomersOrdersListResource, 
                              OrdersResource, AdminOrdersListResource)
from .resources.meals import (FoodListResource, FoodResource)
from .resources.auth import (RegisterResource, LoginResource)

apiv2 = Blueprint('apiv2', __name__)

api2 = Api(apiv2, prefix='/api/v2')

# register v2 endpoints
api2.add_resource(RegisterResource, '/auth/signup')
api2.add_resource(LoginResource, '/auth/login')
api2.add_resource(AdminOrdersListResource, '/orders')
api2.add_resource(CustomersOrdersListResource, '/users/orders')
api2.add_resource(OrdersResource, '/orders/<int:id>')
api2.add_resource(FoodListResource, '/menu')
api2.add_resource(FoodResource, '/meals/<int:id>')

