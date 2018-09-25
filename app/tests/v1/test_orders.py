import pytest
import json
from ... import create_app
from .test_foods import headers

app = create_app(config_name="testing")
client = app.test_client()

order = { 
    "food": "chips",
    "quantity": 2
}
food_item = {
    "name":"chips",
    "price":80
}

empty_order = {}

quantity_less_order = {
 
    "food": "chips"  
}

food_less_order = {
    "quantity": 3, 
}


def test_resource_food_add(): 
    """
        Test post with data
    """
    response = client.post('api/v1/foods', json=food_item, headers=headers)
    assert response.status_code == 200


def test_resource_order_add():
    """
        Test to add post with appropirate data
    """
    response = client.post('api/v1/orders', json=order, headers=headers)
    assert(response.status_code == 201)
    assert 'chips' in str(response.json)

def test_resource_orders_all(): 
    """
        Test to get all orders
    """
    response = client.get('api/v1/orders', headers=headers)
    assert(response.status_code == 200)


def test_resource_order_get_by_id(): 
    """
        Test to get order by its Id
    """
    response = client.get('api/v1/orders/1', headers=headers)
    assert(response.status_code == 200)


def test_resource_order_get_by_id_str(): 
    """
        Test to get order but str for id
    """
    response = client.get('api/v1/orders/e', headers=headers)
    assert(response.status_code == 404)

def test_resource_order_get_by_nonexisting_id(): 
    """
        Test to get order with non-existent id
    """

    response = client.get('api/v1/orders/4', headers=headers)

  


    assert 'exist' in str(response.data)

def test_resource_order_edit(): 
    """
        Test edit by geting right id
    """
    response = client.put('api/v1/orders/1', json ={

        "status": "completed"
    }, headers=headers)
    assert(response.status_code == 201)
    assert 'completed' in str(response.data)

def test_resource_order_edit_invalide_status(): 
    """
        Test edit by geting right id
    """
    response = client.put('api/v1/orders/1', json ={

        "status": "shoe"
    }, headers=headers)
    assert(response.status_code == 422)
    assert 'mark as' in str(response.data)

def test_resource_order_add_without_data(): 
    """
        Test post without data
    """
    response = client.post('api/v1/orders', data=empty_order, headers=headers)
    assert response.status_code == 400

def test_resource_add_without_quantity():
    """
        Test post withot quantity
    """
    response = client.post('api/v1/orders', data=quantity_less_order, headers=headers)
    assert response.status_code == 400

def test_resource_add_without_food():
    """
        Test post withot food
    """
    response = client.post('api/v1/orders', data=food_less_order, headers=headers)
    assert response.status_code == 400