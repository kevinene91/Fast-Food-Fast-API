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

