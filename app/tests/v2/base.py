import unittest
from ... import create_app
from ...api.v2.db.conn import create_db, drop_db


class BaseTest(unittest.TestCase):

    def setUp(self):
        # crete test client
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        # initialize the DB
        with self.app.app_context():
            create_db()

        # test data
        self.user = [{"username": "njoki", "email": "njokiusers@gmail.com",
                     "password": "password"},
                     {"email": "kevine90", "password": "jsjsjjsjs"},
                        {"email": 
                     "testuser@gmail.com", "password": "passsss"}, {},  
                     {'username': 'testuser', 'email': 'testuser@gmail.com', 
                     'password': 'testme'}]

        self.test_user = {'username': 'testuser', 'email': 
                          'testuser@gmail.com', 'password': 'testme'}
        self.meals = [
             {"meal_name": "mayai", "price": 100}, {},
             {"meal_name": "juice", "price": 80}]
        self.orders = [{"meal_id": 1, "quantity": 1}, {},
                       {"quantity": 2, "meal_id": 2}, {'status': 3}]
        self.menu = [{"menu_name": "breakfast"}, {}, {"name": "supper"}]
        self.menuitem = [{"meal_id": 1, "menu_id": 1, "no_available": 1}, {}]

        # create user 
        self.client.post('/api/v2/auth/signup', json=self.user[0])
        response = self.client.post('/api/v2/auth/login', json=self.user[0])
        if response:
            token = response.get_json().get('access_token')
        self.headers = {
                'Authorization': 'Bearer {}'.format(token),
                'Content-Type': 'application/json'
            }

        # login admin user
        response = self.client.post('/api/v2/auth/login', json=self.test_user)
        if response:
            admin_token = response.get_json().get('access_token')
        self.admin_headers = {
                'Authorization': 'Bearer {}'.format(admin_token),
                'Content-Type': 'application/json'
            }

        # ceate meals
        self.client.post('/api/v2/meals', json=self.meals[0],
                         headers=self.admin_headers)
        # create orders
        self.client.post('/api/v2/users/orders', json=self.orders[0],
                         headers=self.headers)  

    def tearDown(self):
        with self.app.app_context():
            drop_db()
