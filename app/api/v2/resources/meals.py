from flask_restful import Resource, reqparse
from flask import jsonify
from ..models.meals import MealModel
from ..middleware.middleware import norm_auth, admin_auth


class FoodResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('meal_name',
                        type=str,
                        required=True)

    parser.add_argument('price',
                        type=str,
                        required=True)
    @norm_auth        
    def get(self, id):
        data = {"meal_id": id}
        meal = MealModel(data).get_by_id()
        message = "no meal with id {}".format(id)
        if meal:
            return jsonify(meal)
        return {"message": message}, 404
        
    @admin_auth
    def put(self, id):
        parsed_data = FoodResource.parser.parse_args()
        data = {"meal_id": id}
        data_to_update = {"meal_name": parsed_data['meal_name'],
                          "price": parsed_data['price'], "meal_id":id}
        menu = MealModel(data).get_by_id()
        if menu:
            MealModel(data_to_update).update_name()
            updated = MealModel(data).get_by_id()
            response = jsonify(updated)
            response.status_code = 201
            return response
        return {"message": "No item to update"}, 404

    @admin_auth
    def delete(self, id):
        data = {"meal_id": id}
        menu = MealModel(data).get_by_id()
        if menu:
            try:
                MealModel(data).delete() 
                crosscheck = MealModel(data).get_by_id()
                if crosscheck:
                    return {"message": " did not deleted"}
                return {"message": "item deleted"}, 202
            except Exception as e:
                print(e)

        return {"message": "item does not exist"}, 404


class FoodListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('meal_name',
                        type=str,
                        required=True)
    
    parser.add_argument('price',
                        type=str,
                        required=True)
    
    @admin_auth
    def post(self):
        data = FoodListResource.parser.parse_args()
        if MealModel(data).get_by_name():
            return {"message": "meal exists"}, 422
        else:
            MealModel(data).save()
            return {"meal_name": data['meal_name'],
                    "price": data['price']}, 201
    
    @norm_auth
    def get(self):
        data = {"table_name": "meals"}
        mylist = MealModel(data).get_all()
        return jsonify(mylist)

