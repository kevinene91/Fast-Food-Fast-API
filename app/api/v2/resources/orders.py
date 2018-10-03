from flask_restful import Resource, reqparse
from flask import jsonify
import simplejson as json
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.orders import OrderModel
from ..middleware.middleware import norm_auth, admin_auth


class CustomersOrdersListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('meal_id',
                        type=int,
                        required=True)

    parser.add_argument('quantity',
                        type=int,
                        required=True)

    @norm_auth
    def post(self):
        parsed_data = CustomersOrdersListResource.parser.parse_args()
        if OrderModel(parsed_data).get_meal_name() is None:
            return {"message": "meal item does not exists"}, 422
        else:
            current_user = get_jwt_identity()
            # user_data = {'user_name':user_name}
            user_id = {'user_id': current_user[0]}
            token_id = current_user[0]
            user_name = OrderModel(user_id).get_user_name()
            meal_name = OrderModel(parsed_data).get_meal_name()
            total = OrderModel(parsed_data).calculate_price()
            data = {'meal_id': parsed_data['meal_id'], 'user_id': token_id,
                    'quantity': parsed_data['quantity'], 'total': total}
            OrderModel(data).save()
            data_to_return = {'meal_name': meal_name['meal_name'], 'ordered_by': user_name['user_name'], 'total':total}
            return (data_to_return), 201

    @norm_auth
    def get(self):
        user_id = get_jwt_identity()[0]
        data = {"user_id": user_id}
        orders = OrderModel(data).get_user_orders()
        return jsonify(orders)


class AdminOrdersListResource(Resource):
    @admin_auth
    def get(self):
        data = {"table_name": "orders"}
        mylist = OrderModel(data).get_all()
        return jsonify(mylist)


class OrdersResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status',
                        type=int,
                        required=True)
                
    # get a specific order 
    @admin_auth
    def get(self, id):
        data = {"order_id": id}
        meal = OrderModel(data).get_by_id()
        message = "no order with {}".format(id)
        if meal:
            return jsonify(meal)
        return {"message": message}, 404

    @admin_auth
    def put(self, id):
        parsed_data = OrdersResource.parser.parse_args()
        expected = [2, 3]
        message = "No order with id {}".format(id)
        if parsed_data['status'] in expected:
            data = {"order_id": id, 'status': parsed_data['status']}
            order = OrderModel(data).get_by_id()
            if order:
                order = OrderModel(data).update_status()
                updated = OrderModel(data).get_by_id()
                response = jsonify(updated)
                response.status_code = 201
                return response
            return {"message": message}, 404
        return {"message": "set to complete or decline"}
        
    @admin_auth
    def delete(self, id):
        data = {"order_id": id}
        order = OrderModel(data).get_by_id()
        if order:
            try:
                OrderModel(data).delete() 
                crosscheck = OrderModel(data).get_by_id()
                if crosscheck:
                    return {"message": " did not deleted"}
                return {"message": "item deleted"}, 202
            except Exception as e:
                print(e)

        return {"message": "item does not exist"}, 404
