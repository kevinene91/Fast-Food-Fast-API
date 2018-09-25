from flask_restful import Resource, reqparse
from ..models.order_model import order_obj

class FoodListResource(Resource):
    def get(self):
        """"
        Return foods list 
        """
        all_foods = order_obj.get_foods()
        if all_foods:
            return all_foods
        return {"message": "no food items present"}, 404

