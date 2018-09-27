import unittest
from ... import create_app
from ...api.v2.db.conn import create_db, drop_db

class BaseTest(unittest.TestCase):

    def generate_headers(self):
        self.reg_data = {
            "username":"testuser", 
            "email": "testuser@gmail.com",
            "password":"password"
        }
        self.client.post('/api/v2/auth/signup', json=self.reg_data)
        response = self.client.post('/api/v2/auth/login', json=self.reg_data)
        if response:
            token = response.get_json().get('access_token')
            headers = {
                'Authorization': 'Bearer {}'.format(token),
                'Content-Type': 'application/json'
            }
            return headers
    
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.headers = self.generate_headers()
        self.user=[ {"username":"testuser",  "email": "testuser@gmail.com","password":"password"},{},
        {"email": "testuser@gmail.com","password":"passsss"}, {"email": "test@gmail.com","password":"password"}
        ]
        self.meals =[{"name":"maziwa","price":80}, {}, {"name":"juice","price":80},
            {} ]
        self.orders=[{"user_id":1,"total":300,"status":1,"menuitem_id":1},{},{"user_id":2,"total":300,"status":2,"menuitem_id":2}]
        self.menu= [{"name":"breakfast"}, {},{"name":"supper"}, {}]
        self.menuitem=[{"meal_id":1,"menu_id":1,"no_available":1},{}]

        with self.app.app_context():
            self.db = create_db

    def tearDown(self):
         with self.app.app_context():
              drop_db()
              
        
             
                                