import pytest
import json
from ... import create_app

app = create_app(config_name="testing")
client = app.test_client()

empty_food_item= {}
price_less_order= {
    "name":"maziwa"
}

name_less_order = {
    "price": 80
}

def test_resource_orders_all(): 
    """
        Test to get all orders
    """
    response = client.get('api/v1/foods')
    assert(response.status_code == 200)

def test_resource_order_get_by_id(): 
    """
        Test to get order by its Id
    """
    response = client.get('api/v1/foods/1')
    assert(response.status_code == 200)

def test_resource_foods_get_by_id_str(): 
    """
        Test to get order but str for id
    """
    response = client.get('api/v1/foods/e')
    assert(response.status_code == 405)

def test_resource_foods_get_by_nonexisting_id(): 
    """
        Test to get order with non-existent id
    """
    response = client.get('api/v1/foods/4')
    assert 'exist' in str(response.data)
def test_resource_order_add_without_data(): 
    """
        Test post without data
    """
    response = client.post('api/v1/foods', data=empty_food_item)
    assert response.status_code == 400

def test_resource_add_without_name():
    """
        Test post withot quantity
    """
    response = client.post('api/v1/foods', data=name_less_order)
    assert response.status_code == 400

def test_resource_add_without_price():
    """
        Test post withot food
    """
    response = client.post('api/v1/foods', data=price_less_order)
    assert response.status_code == 400


def test_resource_order_edit(): 
    """
        Test edit by geting right id
    """
    response = client.put('api/v1/foods/1', data ={
        "name": "chips",
        "price": 200
    })
    assert(response.status_code == 201)
    assert 'chips' in str(response.data)
