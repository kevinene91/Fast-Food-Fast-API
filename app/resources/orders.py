
from flask_restful import Resource
from app.models import orders

class OrderListResource(Resource):
    def get(self): 
        return {'orders':orders}

