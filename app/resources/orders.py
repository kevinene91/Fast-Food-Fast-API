
from flask_restful import Resource, reqparse
from app.models import order_obj

class OrderListResource(Resource):

	def get(self): 

		"""
		Return all the orders 
		"""
		allorders = order_obj.get_orders()
		return {"orders":allorders}
		

	def post(self):
		"""
		Post an order fields input, food, quantity, price, status
		"""
		inc_id = order_obj.get_length() + 1
		parser = reqparse.RequestParser()
		parser.add_argument("food",type=str,
		required=True)
		parser.add_argument("quantity",type=int,
		required=True)
		data = parser.parse_args()

		food_item = order_obj.get_food_by_name(data['food'],order_obj.get_foods())
		food_price = food_item['price']   
		total = order_obj.calculate_total_price(food_price,data['quantity'])
		
		order = {
		'id': inc_id, "customer_name":"nesh",'food':data['food'],
		'quantity':data['quantity'],'total':total,
		'status':"pending" 
		}
		order_obj.add_order(order)
		return order, 201


class OrderResource(Resource): 
	def get(self,id):
		"""
			get a specicfic order via its id
		"""
		#filter list elements that do no have the id 
		return order_obj.get_by_id(id,order_obj.get_orders())


	def put(self,id):
		"""
			get an order by its id and update it
		"""
		# get input
		parser = reqparse.RequestParser()
		parser.add_argument("status",
				type=str,
				required=True,
		)
		data = parser.parse_args()
		order_to_edit = order_obj.get_by_id(id,order_obj.get_orders())

		#update order if found
		if order_to_edit:
			order_to_edit.update(data)
		else:
			return {"message":"no item to update"}, 400
		return order_to_edit, 201

