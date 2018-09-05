
from flask_restful import Resource, reqparse
from app.models import orders

class OrderListResource(Resource):
    
    
    def get(self): 
        return {'orders':orders}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id",
                type=int, 
                required=True,
        )
        parser.add_argument("food",
                type=str,
                required=True,
        )
        parser.add_argument("quantity",
                type=int,
                required=True,
        )
        parser.add_argument("price",
                type=int,
                required=True,
        )
        parser.add_argument("status",
                type=str,
                required=True,
        )
        data = parser.parse_args()
        order = {
            'id': data['id'], 'food':data['food'],
            'quantity':data['quantity'],'price':data['price'],
            'status':data['status'] 
                }
        orders.append(order)
        return order

        

class OrderResource(Resource): 
	def get(self,id):
		return {'order': next(filter(lambda x:x['id'] == id, orders), None)}

	def put(self,id):
		parser = reqparse.RequestParser()
		parser.add_argument("status",
				type=str,
				required=True,
		)
		data = parser.parse_args()
		order_to_edit = next(filter(lambda x:x['id'] == id, orders), None)
		if order_to_edit:
			order_to_edit.update(data)
		return order_to_edit


    