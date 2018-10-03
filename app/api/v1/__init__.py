from flask import Blueprint
from flask_restful import Api
from .resources.orders import (OrderListResource, OrderResource)

from .resources.foods import (FoodListResource, FoodResource,
                             ChangePriceResource)

from .resources.auth import (RegisterResource, LoginResource, 
                            LogoutResource)

apiv1 = Blueprint('apiv1', __name__)

api = Api(apiv1, prefix='/api/v1')

# register the endpoints

api.add_resource(OrderListResource, '/orders')
api.add_resource(OrderResource, '/orders/<int:id>')
api.add_resource(FoodListResource, '/foods')
api.add_resource(FoodResource, '/foods/<int:id>')
api.add_resource(ChangePriceResource, '/foods/<string:name>')
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')



