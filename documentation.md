FORMAT: 1A
HOST: https://fast-food-place.herokuapp.com/api/v1

# Fast-Food-API-V2
Fast-Food-API-v2 Documentation



## Authentication
This API uses OAuth v2 Bearer Token / Personal Access Token for its authentication.

# Group Auth

## Signup [/signup]

### https://fast-food-place.herokuapp.com/api/v1/signup [POST]
User registration endpoint 

required fileds 

username 

email

password

+ Request (application/json)
    + Attributes (https://fast-food-place.herokuapp.com/api/v1/signup )

    + Body

            {
                "username": "josem",
                "email": "jose@gml.com",
                "password": "andela"
            }


+ Response 200 




## Auth Login [/auth/login]

### httpsfastfoodplace.herokuapp.comapiv2authsignup Copy [POST]
User login endpoint 

required fields 



email

password

+ Request (application/json)
    + Attributes (httpsfastfoodplace.herokuapp.comapiv2authsignup CopyRequest)

    + Body

            {
                "email": "paul@gmail.com",
                "password": "andela"
            }


+ Response 200 





# Group Menu

## Menu [/menu]

### httpsfastfoodplace.herokuapp.comapiv2menu [POST]
Admin post Menu endpoint 



Admin Auth required 

admin credentials 

 {"email": "testuser@gmail.com", 

                     "password": "testme"}

required fileds 



meal_name

price

+ Request (application/json)
    + Attributes (httpsfastfoodplace.herokuapp.comapiv2menuRequest)

    + Body

            {
                "meal_name": "Pizza",
                "price": 100
            }


+ Response 200 



### httpsfastfoodplace.herokuapp.comapiv2menu Copy [POST]
Admin post Menu endpoint 



Admin Auth required 

admin credentials 

 {"email": "testuser@gmail.com", 

                     "password": "testme"}

required fileds 



meal_name

price

+ Request (application/json)
    + Attributes (httpsfastfoodplace.herokuapp.comapiv2menuRequest)

    + Body

            {
                "meal_name": "Pizza",
                "price": 100
            }


+ Response 200 



### httpsfastfoodplace.herokuapp.comapiv2menu [GET]
GET Menu endpoint 



Normal user Auth required

+ Request (application/json)



+ Response 200 




## Meals 1 [/meals/1]

### httpsfastfoodplace.herokuapp.comapiv2menu1 [GET]
GET Menu item endpoint 



Normal user Auth required

+ Request (application/json)



+ Response 200 



### httpsfastfoodplace.herokuapp.comapiv2menu1 [PUT]
Admin edit Menu endpoint 



Admin Auth required 



admin credentials 

 {"email": "testuser@gmail.com", 

                     "password": "testme"}

editable fileds 



meal_name

price

+ Request (application/json)
    + Attributes (httpsfastfoodplace.herokuapp.comapiv2menuRequest)

    + Body

            {
                "meal_name": "Pizza",
                "price": 100
            }


+ Response 200 



### httpsfastfoodplace.herokuapp.comapiv2menu1 [DELETE]
Admin delete Menu endpoint 



Admin Auth required 



admin credentials 

 {"email": "testuser@gmail.com", 

                     "password": "testme"}

+ Request (application/json)
    + Attributes (httpsfastfoodplace.herokuapp.comapiv2menuRequest)

    + Body

            {
                "meal_name": "Pizza",
                "price": 100
            }


+ Response 200 





# Group Orders

## Users Orders [/users/orders]

### httpsfastfoodplace.herokuapp.comapiv2usersorders [POST]
Users post endpoint



normal user Auth required 



required fields

{

    "meal_id":"2",

    "quantity":2

}

+ Request (application/json)
    + Attributes (httpsfastfoodplace.herokuapp.comapiv2usersordersRequest)

    + Body

            {
                "meal_id": "2",
                "quantity": 2
            }


+ Response 200 



+ Response 400 

        BAD REQUEST



    + Body

            {"message":{"meal_id":"Missing required parameter in the JSON body or the post body or the query string"}}


### httpsfastfoodplace.herokuapp.comapiv2usersorders [GET]
Get Users endpoint



normal user Auth required

+ Request (application/json)



+ Response 200 




## Orders 1 [/orders/1]

### httpsfastfoodplace.herokuapp.comapiv2usersorders1 [PUT]
Edit Users endpoint



Admin Auth required 



Admin credentials

{

    "email":"testuser@gmail.com",

    "password":"testme"

}

+ Request (application/json)
    + Attributes (httpsfastfoodplace.herokuapp.comapiv2usersorders1Request)

    + Body

            {
                "status": "2"
            }


+ Response 200 



### httpsfastfoodplace.herokuapp.comapiv2orders1 [GET]
Get specif order



Admin Auth required 



Admin credentials

{

    "email":"testuser@gmail.com",

    "password":"testme"

}

+ Request (application/json)



+ Response 200 





# Data Structures

## httpsfastfoodplace.herokuapp.comapiv2authsignupRequest (object)


### Properties
+ `username`: `josem` (string, required) 
+ `email`: `jose@gml.com` (string, required) 
+ `password`: `andela` (string, required) 


## httpsfastfoodplace.herokuapp.comapiv2authsignup CopyRequest (object)


### Properties
+ `email`: `paul@gmail.com` (string, required) 
+ `password`: `andela` (string, required) 


## httpsfastfoodplace.herokuapp.comapiv2menuRequest (object)


### Properties
+ `meal_name`: `Pizza` (string, required) 
+ `price`: `100` (number, required) 


## httpsfastfoodplace.herokuapp.comapiv2usersordersRequest (object)


### Properties
+ `meal_id`: `2` (string, required) 
+ `quantity`: `2` (number, required) 


## httpsfastfoodplace.herokuapp.comapiv2usersordersErrorResponse (object)


### Properties
+ `message` (Message, required) 


## Message (object)


### Properties
+ `meal_id`: `Missing required parameter in the JSON body or the post body or the query string` (string, required) 


## httpsfastfoodplace.herokuapp.comapiv2usersorders1Request (object)


### Properties
+ `status`: `2` (string, required) 

