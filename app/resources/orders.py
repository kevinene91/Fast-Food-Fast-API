
from flask_restful import Resource
from app.models import orders

class OrderListResource(Resource):
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

    