
from flask_restful import Resource, reqparse
from app.models import orders

class OrderListResource(Resource):

	def get(self): 

		"""
		Return all the orders 
		"""
		return {'orders':orders}

	def post(self):
		"""
		Post an order fields input, food, quantity, price, status
		"""
		inc_id = len(orders) + 1
		parser = reqparse.RequestParser()
		parser.add_argument("food",type=str,
		required=True)
		parser.add_argument("quantity",type=int,
		required=True)
		parser.add_argument("price",type=int,
		required=True)
		parser.add_argument("status",type=str,
		required=True)
		data = parser.parse_args()
		order = {
		'id': inc_id, 'food':data['food'],
		'quantity':data['quantity'],'price':data['price'],
		'status':data['status'] 
		}
		orders.append(order)
		return order, 201


class OrderResource(Resource): 
	def get(self,id):
		"""
			get a specicfic order via its id
		"""
		#filter list elements that do no have the id 
		return {'order': next(filter(lambda x:x['id'] == id, orders), None)}

	def get(self):
		"""
			return all the orders
		"""
		return {'orders':orders}


class OrderResource(Resource): 
    """
		get specific order via its id
	"""
    def get(self,id):
        return {'order': next(filter(lambda x:x['id'] == id, orders), None)}


    