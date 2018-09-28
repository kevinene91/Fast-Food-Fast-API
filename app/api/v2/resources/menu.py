from flask_restful import Resource, reqparse
from flask import jsonify
from ..models.menu import MenuModel

class MenuResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('menu_name',
    type = str,
    required = True)
    
    def get(self,id):
        data = {"meal_id":id}
        menu = MenuModel(data).get_by_id()
        message = "no  with {}".format(id)
        if menu:
            return jsonify(menu)
        return {"message":message}, 404
    
    def put(self,id):
        parsed_data = MenuResource.parser.parse_args()
        data_to_update={"menu_name":parsed_data['menu_name'], "menu_id":id}
        data = {"menu_id":id}
        menu = MenuModel(data).get_by_id()
        if menu:
            updated = MenuModel(data_to_update).update_name()
            return jsonify(updated)
        return {"message":"No item to update"}, 404

    def delete(self,id):
        data = {"menu_id":id}
        menu = MenuModel(data).get_by_id()
        if menu:
            try:
                MenuModel(data).delete()
                crosscheck = MenuModel(data).get_by_id()
                if crosscheck:
                    return {"message":"deleted"}
                return {"message":"did not delete"}
            except Exception as e:
                print(e)

        return {"message":"item does not exist"}


class MenuListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('menu_name',
    type = str,
    required = True)
       
    def post(self):
        data = MenuListResource.parser.parse_args()
        if MenuModel(data).get_by_name():
            return {"message":"menu exists"}, 404
        else:
            return {"menu_name":data['menu_name']}, 200
    
    def get(self):
        data ={"table_name":"menus"}
        mylist = MenuModel(data).get_all()
        return jsonify(mylist)
        

 