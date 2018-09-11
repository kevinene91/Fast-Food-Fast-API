import pytest
import json
from app import create_app

app = create_app(config_name="testing")
client = app.test_client()

order = {

    "food": "chips",
    "quantity": 2, 
}

empty_order = {}

quantity_less_order = {
 
    "food": "chips", 
   
}

food_less_order = {
    "quantity": 3, 
}

        








            


def test_resource_orders_all(): 
    """
        Test to get all orders
    """
    response = client.get('api/v1/orders')
    assert(response.status_code == 200)

def test_resource_order_add():
    """
        Test to add post with appropirate data
    """
    response = client.post('api/v1/orders', data=order)
    assert(response.status_code == 201)
    assert 'chips' in str(response.data)

def test_resource_order_add_without_data(): 
    """
        Test post without data
    """
    response = client.post('api/v1/orders', data=empty_order)
    assert response.status_code == 400

def test_resource_add_without_quantity():
    """
        Test post withot quantity
    """
    response = client.post('api/v1/orders', data=quantity_less_order)
    assert response.status_code == 400

def test_resource_add_without_food():
    """
        Test post withot food
    """
    response = client.post('api/v1/orders', data=food_less_order)
    assert response.status_code == 400

def test_resource_order_get_by_id(): 
    """
        Test to get order by its Id
    """
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

def test_resource_order_edit(): 
    """
        Test edit by geting right id
    """
    response = client.put('api/v1/orders/1', data ={
        "id": 5,
        "food": "chips",
        "quantity": 2, 
        "price": 200,
        "status": "completed"
    })
    assert(response.status_code == 201)
    assert 'completed' in str(response.data)
