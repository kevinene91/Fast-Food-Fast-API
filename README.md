

[![Coverage Status](https://coveralls.io/repos/github/kevinene91/Fast-Food-Fast-API/badge.svg?branch=develop )](https://coveralls.io/github/kevinene91/Fast-Food-Fast-API?branch=develop)[![Build Status](https://travis-ci.org/kevinene91/Fast-Food-Fast-API.svg?branch=develop)](https://travis-ci.org/kevinene91/Fast-Food-Fast-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/67c0f234dca2f9a3bd78/maintainability)](https://codeclimate.com/github/kevinene91/Fast-Food-Fast-API/maintainability)

### Flask FAST FOOD FAST
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

API Endpoints 

|   # Endpoint     |  # Methods | # Description       |
| -------------    |----------- | ------------------  | 
|/api/v1/orders    |   GET      |  list all orders    |
| ------------     | ---------- | -----------------   |
|/api/v1/order/<id>|   GET      | get a specific order|
| -------------    | ---------  | ------------------- |
|/api/v1/orders    |   POST     | add  a new order    |
|--------------    |----------- | -----------------   |
|/api/v1/order/<id>|   PUT      |edit the order-status|
