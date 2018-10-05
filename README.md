
# Fast-Food-Fast-API 
FastFood API is a REST API that fetches that allows its user to order for food
### Coveralls 
[![Coverage Status](https://coveralls.io/repos/github/kevinene91/Fast-Food-Fast-API/badge.svg?branch=develop )](https://coveralls.io/github/kevinene91/Fast-Food-Fast-API?branch=develop )
### Travis badge 
[![Build Status](https://travis-ci.org/kevinene91/Fast-Food-Fast-API.svg?branch=develop)](https://travis-ci.org/kevinene91/Fast-Food-Fast-API)

This is a Flask Restful API for an app that allows customers to place orders 

### Installation and Setup 
Clone the repo 

`git clone https://github.com/kevinene91/Fast-Food-Fast-API.git`

Switch the develop branch 

`git fetch origin develop`

Navigate to the folder 

`cd Fast-Food-API`

create a virual env 

`virtualenv venv`

Activate the venv 

`source/venv/activate`

Install the required packages 

`pip install -r requirements.txt`

### Launch the program 

`python run.py`

Use Postman to the test the following endpoints 

# API Auth


|Endpoint           |   Method   | description         |
|  ------------     | ---------- |  -----------------  |
|/api/v2/auth/signup|   POST     | add  a new user     |
|                   |            |                     |
|/api/v2/auth/login |   POST     |User Login token     |
|                   |            |                     | 
|/api/v2/auth/logout|   POST     | User logout         |

# API Endpoints

|   # Endpoint       |  # Methods | # Description       |Auth Required  |
|   -----------      | ---------- | -----------------   | ------------  |
|/api/v2/menu        |   GET      |  list all foods     |    user       |
|                    |            |                     |               | 
|/api/v2/menu        |   POST     | add  a new food     |    admin      |
|                    |            |                     |               |
|/api/v2/meals/<id>  |   PUT      |edit the food-item   |    admin      |
|                    |            |                     |               |
|/api/v2/order/<id>  |   GET      | get a specific order|    admin      |
|                    |            |                     |               |
|/api/v2/users/orders|   POST     | add  a new order    |    user       |
|                    |            |                     |               |
|/api/v1/order/<id>  |   PUT      |edit the order-status|    admin      |
|                    |            |                     |               |
|/api/v2/users/orders|   GET      | list all orders     |    user       |
|                    |            |                     |               | 
|/api/v2/orders      |   GET      |   List all order    |   admin       |

### API DOCUMENTATION 

[Documentation](https://fastfoodfast1.docs.apiary.io/#reference/menu/meals-1)

### HEROKU LINK
[HEROKU API](https://fast-food-place.herokuapp.com/)

### Author 

# Kevin Munene