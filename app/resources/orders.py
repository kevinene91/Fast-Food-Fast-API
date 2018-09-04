
from flask_restful import Resource
from app.models import orders

class OrderListResource(Resource):
    def get(self): 
        return {'orders':orders}


class OrderResource(Resource): 
    
    def get(self,id):
        return {'order': next(filter(lambda x:x['id'] == id, orders), None)}

    