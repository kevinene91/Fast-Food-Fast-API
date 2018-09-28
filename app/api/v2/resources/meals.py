from flask_restful import Resource, reqparse
from flask import jsonify
import simplejson as json

from ..models.meals import MealModel

class FoodResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('meal_name',
    type = str,
    required = True)

    parser.add_argument('price',
    type = int,
    required = True)

    
    def get(self,id):
        data = {"meal_id":id}
        meal = MealModel(data).get_by_id()
        message = "no meal with {}".format(id)
        if meal:
            return jsonify(meal)
        return {"message":message}, 404
    
    def put(self,id):
        parsed_data = FoodResource.parser.parse_args()
        data_to_update={"meal_name":parsed_data['meal_name'], "meal_id":id}
        data = {"meal_id":id}
        menu = MealModel(data).get_by_id()
        if menu:
            updated = MealModel(data_to_update).update_name()
            return jsonify(updated)
        return {"message":"No item to update"}, 404

    def delete(self,id):
        data = {"meal_id":id}
        menu = MealModel(data).get_by_id()
        if menu:
            try:
                MealModel(data).delete()
                crosscheck = MealModel(data).get_by_id()
                if crosscheck:
                    return {"message":"deleted"}
                return {"message":"did not delete"}
            except Exception as e:
                print(e)

        return {"message":"item does not exist"}

class FoodListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('meal_name',
    type = str,
    required = True)

    parser.add_argument('price',
    type = int,
    required = True)
       
    def post(self):
        data = FoodListResource.parser.parse_args()
        if MealModel(data).get_by_name():
            return {"message":"menu exists"}, 404
        else:
            MealModel(data).save()
            return {"meal_name":data['meal_name'],"meal_price":data['price']}, 200
    
    def get(self):
        data ={"table_name":"meals"}
        mylist = MealModel(data).get_all()
        return jsonify(mylist)    

