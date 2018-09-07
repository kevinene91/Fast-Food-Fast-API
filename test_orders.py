import pytest
import json
from app import create_app

app = create_app(config_name="testing")
client = app.test_client()
order = {
    "id": 1,
    "food": "chips",
    "quantity": 2, 
    "price": 200,
    "status": "pending"
}

def test_resource_orders_all(): 
    response = client.get('api/v1/orders')
    assert(response.status_code == 200)


    

        




