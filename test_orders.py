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
    
def test_resource_order_get_by_id(): 
    response = client.get('api/v1/orders/1')
    assert(response.status_code == 200)

def test_resource_order_get_by_id_str(): 
    """
        Test to get order but str for id
    """
    response = client.get('api/v1/orders/e')
    assert(response.status_code == 404)

def test_resource_order_get_by_nonexisting_id(): 
    """
        Test to get order with non-existent id
    """
    response = client.get('api/v1/orders/4')
    assert 'null' in str(response.data)

def test_resource_order_get_by_negative_id(): 
    """
        Test to get order with negative id
    """
    response = client.get('api/v1/orders/-4')
    assert response.status_code == 404

        




