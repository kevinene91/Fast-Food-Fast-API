import unittest
import json 
from app import create_app


class OrdersTestCase(unittest.TestCase): 

    def setUp(self): 
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.order = {
            "food": "chips",
            "quantity": 2, 
            "price": 200,
            "status": "pending"
        }

    def test_resource_orders_all(self): 
        response = self.client.get('api/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_resource_order_add(self):
        response = self.client.post('api/v1/order', data=json.dumps(self.order))
        self.assertEqual(response.status_code, 201)

    def test_resource_order_get_by_id(self): 
        response = self.client.get('api/v1/order/1')
        self.assertEqual(response.status_code, 200)

    def test_resource_order_edit(self): 
        # get_order_to_edit = self.client.get('api/v1/order/1')
        response = self.client.put('api/v1/order/1', data ={
            "food": "chips",
            "quantity": 2, 
            "price": 200,
            "status": "completed"
        })
        self.assertEqual(response.status_code, 201)
        result = self.client.get('api/v1/order/1')
        self.assertIn('complted', str(result.data))
        

if __name__ == "__main__":
    unittest.main()



