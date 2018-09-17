"""
    Database
    List with dictionairies emulates a database table
"""
class OrderModel(object ):
    existing_data = []

    def __init__(self):
       self.orders = []
       self.foods =  []
    """
    Model Managers
    """
    # get all orders
    def get_orders(self):
        return self.orders
    
    #get all food items
    def get_foods(self): 
        return self.foods

    #populated orders data in database
    def saved_orders_list_database(self, data):
        for i in data:
            ext_database = self.orders.append(i)
        return ext_database

    #populated foods data in database
    def saved_food_list_database(self, data):
        for i in data:
            ext_food_table = self.foods.append(i)
        return ext_food_table
    
    #add an order to table
    def add_order(self,data):
        self.orders.append(data)

    #quert by name
    def get_food_by_name(self, name,data):
        return next(filter(lambda x:x['name'] == name, data), None)
    
    #get total price
    def calculate_total_price(self, price, quantity):
        return price * quantity

    # get list length for  auto-increment 
    def get_length(self):
        data_len = len(self.orders)
        return data_len

    # query by id
    def get_by_id(self,id,data):
        return next(filter(lambda x:x['id'] == id, data), None)

                   
orders =[
    {
        "id": 1,
        "customer": "nesh",        
         "food": [
            {"name": "chai", 
            "price": 60,
            "quantity": 2
            },
            {"name": "kuku", 
            "price": 300 ,
            "quantity": 2}
         ], 
         "total": 360,
         "status": "pending"   
    },
    {
        "id": 2, 
        "customer": "nesh",       
        "food": [
             {"name": "chai", 
            "price": 60,
            "quantity": 2
            },
            {"name": "kuku", 
            "price": 300 ,
            "quantity": 2}
        ],
        "quantity": 3, 
        "total": 360,
        "status": "pending" 
    }
]


foods = [
        {
            "id": 1,
            "name": "chai", 
            "price": 60
        },

        {
            "id":2,
            "name": "kuku", 
            "price": 300

        }, 
        {
            "id":3,
            "name": "chips",
            "price": 200
        }

    ]

#class instance
order_obj = OrderModel()

order_obj.saved_orders_list_database(orders)
order_obj.saved_food_list_database(foods)