import pytest
import json
from ... import create_app
from .test_foods import headers

app = create_app(config_name="testing")
client = app.test_client()
list_for_test_data = [
{
"username": "pius",
"password": "thething",
"email": "kevinene91@gmail.com",
"address": "rwambiti"
},
{
    "username":"pius",
    "password":"thething"
},
{
},
{
    "username":"pius",
},
{
    "password":"thething"
}, 
{
    "username":"pius",
    "password":"theing"
}, 
{
"username": "pius",
"password": "thething",
"email": "kevinene91@gmail",
"address": "rwambiti"
}

]


#test register a new user 
def test_register():
    response = client.post('/api/v1/register', json=list_for_test_data[0])
    assert response.status_code == 200

# #test register a new user 
# def test_register_with_invalid_email():
#     response = client.post('/api/v1/register', json=list_for_test_data[6])
#     assert response.status_code == 400

#test register an already existing user 
def test_register_user_exist_data():
    response = client.post('/api/v1/register', json=list_for_test_data[0])
    assert response.status_code == 200
    assert 'already registered' in str(response.json)

#test register an already existing user 
def test_register_without_data():
    response = client.post('/api/v1/register', json=list_for_test_data[2])
    assert response.status_code == 400

#test login 
def test_login():
    response = client.post('/api/v1/login', json=list_for_test_data[1])
    assert response.status_code == 200

#test login without data
def test_login_without_data():
    response = client.post('/api/v1/login', json=list_for_test_data[2])
    assert response.status_code == 400

#test login without passwrd
def test_login_without_password():
    response = client.post('/api/v1/login', json=list_for_test_data[3])
    assert response.status_code == 400

#test login without username
def test_login_without_username():
    response = client.post('/api/v1/login', json=list_for_test_data[4])
    assert response.status_code == 400

#test with wrong credentials
def test_with_wrong_password():
    response = client.post('/api/v1/login', json=list_for_test_data[5])
    assert response.status_code == 401
    assert 'invalid' in str(response.json)

#test logout
def test_logout():
    response = client.post('/api/v1/logout',headers=headers)
    assert response.status_code == 200
    assert 'logged out' in str(response.json)