
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

food_item = {
    "name":"maziwa",
    "price":80
}

another_item = {
    "name": "ngwaci",
    "price": 500
}

dummy_user = {	
    "username":"pius",
	"email":"kevinene91@gmail.com",
	"password":"thething",
	"address":"rwambiti"
}
regsiter_data = {
"username": "pius",
"password": "thething",
"email": "kevinene91@gmail.com",
"address": "rwambiti"
}
login_data ={
    "username":"pius",
    "password":"thething"
}

def login_user():
    client.post('api/v1/register', json=regsiter_data)
    user = client.post('api/v1/login', json=login_data) 
    token =  user.get_json().get('access_token')
    return token

token = login_user()

headers = {
    'Authorization': 'Bearer {}'.format(token),
    'Content-Type': 'application/json'
}

def test_resource_food_add(): 
    """
        Test post with data
    """
    
    response = client.post('api/v1/foods', json=food_item, headers=headers)
    assert response.status_code == 200

def test_resource_foods_all(): 
    """
        Test to get all orders

    """
  
    response = client.get('api/v1/foods', headers=headers)
    assert(response.status_code == 200)

def test_resource_order_get_by_id(): 
    """
        Test to get order by its Id
    """
    response = client.get('api/v1/foods/1', headers=headers)
    assert(response.status_code == 200)

def test_resource_foods_get_by_id_str(): 
    """
        Test to get order but str for id
    """
    response = client.get('api/v1/foods/e', headers=headers)
    assert(response.status_code == 405)

def test_resource_foods_get_by_nonexisting_id(): 
    """
        Test to get order with non-existent id
    """
    response = client.get('api/v1/foods/4', headers=headers)
    assert 'exist' in str(response.data)


def test_resource_food_edit(): 
    """
        Test edit by geting right id
    """
    response = client.put('api/v1/foods/1', json ={
        "name": "maziwa",
        "price": 200
    }, headers=headers)
    assert(response.status_code == 201)
    assert 'maziwa' in str(response.json)

def test_resource_food_delete():
    """
        Test delete item
    """
    client.post('api/v1/foods', data=another_item)
    response = client.delete('api/v1/foods/1', headers=headers)
    assert(response.status_code == 202)
    assert 'deleted' in str(response.data)


def test_resource_order_add_without_data(): 
    """
        Test post without data
    """
    response = client.post('api/v1/foods', data=empty_food_item, headers=headers)
    assert response.status_code == 400

def test_resource_add_without_name():
    """
        Test post withot quantity
    """
    response = client.post('api/v1/foods', data=name_less_order, headers=headers)
    assert response.status_code == 400

def test_resource_add_without_price():
    """
        Test post withot food
    """
    response = client.post('api/v1/foods', data=price_less_order, headers=headers)
    assert response.status_code == 400