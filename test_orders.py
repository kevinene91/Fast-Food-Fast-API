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

def test_resource_order_add():
    response = client.post('api/v1/orders', data=order)
    assert(response.status_code == 200)
    
def test_resource_order_get_by_id(): 
    response = client.get('api/v1/orders/1')
    assert(response.status_code == 200)

def test_resource_order_edit(): 
    response = client.put('api/v1/orders/1', data ={
        "id": 5,
        "food": "chips",
        "quantity": 2, 
        "price": 200,
        "status": "completed"
    })
    assert(response.status_code == 200)
    

        




