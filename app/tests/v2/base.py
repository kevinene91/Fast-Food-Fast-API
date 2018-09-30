import unittest
from ... import create_app
from ...api.v2.db.conn import create_db, drop_db

class BaseTest(unittest.TestCase):

    def setUp(self):
        #crete test client
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        #initialize the DB
        with self.app.app_context():
            create_db()
        
        #test data
        self.user=[ {"username":"njoki", "email": "njokiusers@gmail.com","password":"password"},{},
        {"email": "testuser@gmail.com","password":"passsss"}, {"email": "test@gmail.com","password":"password"}]
        self.meals =[{"meal_name":"sausage","price":80}, {}, {"meal_name":"juice","price":80}]
        self.orders=[{"user_id":1,"total":300,"status":1,"menuitem_id":1},{},{"user_id":2,"total":300,"status":2,"menuitem_id":2}]
        self.menu= [{"menu_name":"breakfast"}, {},{"name":"supper"}]
        self.menuitem=[{"meal_id":1,"menu_id":1,"no_available":1},{}]
        #create user 
        self.client.post('/api/v2/auth/signup', json=self.user[0])
        response = self.client.post('/api/v2/auth/login', json=self.user[0])
        if response:
            token = response.get_json().get('access_token')
        self. headers = {
                'Authorization': 'Bearer {}'.format(token),
                'Content-Type': 'application/json'
            }
      

    def tearDown(self):
         with self.app.app_context():
              drop_db()
              
        
             
                                