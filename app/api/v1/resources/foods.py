from flask_restful import Resource, reqparse
from ..models.order_model import order_obj

class FoodListResource(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("name",type=str,
    required=True)

    parser.add_argument("price",type=int,
    required=True)
   
		
    def get(self):
        """"
        Return foods list 
        """
        all_foods = order_obj.get_foods()
        if all_foods:
            return all_foods
        return {"message": "no food items present"}, 404

    def post(self):
        """
        Post foods  
        """
        inc_id = order_obj.get_length(order_obj.get_foods()) + 1
        data = FoodListResource.parser.parse_args()
        food_item = order_obj.get_food_by_name(data['name'],order_obj.get_foods())
        if food_item:
            return {'message': 'food item already added try another'}

        else:
            food = {
                'id': inc_id, 'name': data['name'], 'price':data['price']
            }
            return food
       

class FoodResource(Resource):
    def get(self,id):
        """
        Return a specific food item by id
        """
        food = order_obj.get_by_id(id,order_obj.get_foods())
        if food:
            return food, 200
        return {"message": "food item does not exist"}, 404

    