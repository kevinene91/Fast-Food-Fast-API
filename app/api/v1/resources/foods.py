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

class FoodResource(Resource):
    def get(self,id):
        """
        Return a specific food item by id
        """
        food = order_obj.get_by_id(id,order_obj.get_foods())
        if food:
            return food, 200
        return {"message": "food item does not exist"}, 404

    