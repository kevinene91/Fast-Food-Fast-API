
from flask_restful import Resource, reqparse
from ..models.order_model import order_obj
from flask import jsonify

class OrderListResource(Resource):

	def get(self): 

		"""
		Return all the orders 
		"""
		allorders = order_obj.get_orders()
		if allorders:
			return allorders
		else:
			return {"mesage":"no orders present"}
		

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
		
		#check if food is in menu
		food_item = order_obj.get_food_by_name(data['food'],order_obj.get_foods())
		if food_item:
			food_price = food_item['price']   
			total = order_obj.calculate_total_price(food_price,data['quantity'])
			#add default order items
			order = {
			'id': inc_id, "customer_name":"nesh",'food':data['food'],
			'quantity':data['quantity'],'total':total,
			'status':"pending" 
			}
			order_obj.add_order(order)
			return order, 201
		else:
			return {'message': 'no such food item in menu'}, 404


class OrderResource(Resource): 
	def get(self,id):
		"""
			get a specicfic order via its id
		"""
		#filter list elements that do no have the id 
		order = order_obj.get_by_id(id,order_obj.get_orders())
		if order:
			return order, 200
		else:
			message =  "order {} does not exist".format(id)
			return {"message":message}, 404


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

 