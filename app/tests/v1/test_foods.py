import pytest
import json
from ... import create_app

app = create_app(config_name="testing")
client = app.test_client()


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

def test_resource_order_get_by_id_str(): 
    """
        Test to get order but str for id
    """
    response = client.get('api/v1/foods/e')
    assert(response.status_code == 404)

def test_resource_order_get_by_nonexisting_id(): 
    """
        Test to get order with non-existent id
    """
    response = client.get('api/v1/foods/4')
    assert 'exist' in str(response.data)
