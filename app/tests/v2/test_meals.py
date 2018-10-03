import unittest
from .base import BaseTest


class MealsTestCase(BaseTest):

    def test_food_resource_add(self):
        response = self.client.post('api/v2/menu', json=self.meals[2], 
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)

    def test_food_resource_add_existing_food(self):
        response = self.client.post('api/v2/menu', json=self.meals[0],
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 422)
        self.assertIn('exists', str(response.json)) 

    def test_food_resource_get_specific(self):
        response = self.response = self.client.get('api/v2/meals/1',
                                                   headers=self.headers)
        self.assertEqual(response.status_code, 200)
    
    def tes_food_resource_get_all(self):
        response = self.response = self.client.get('api/v2/menu', 
                                                   headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_food_resource_get_non_existent(self):
        response = self.response = self.client.get('api/v2/meals/56', 
                                                   headers=self.headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('no meal', str(response.json))

    def test_food_resource_edit_non_existent(self):
        response = self.client.put('api/v2/meals/56', json=self.meals[0],
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('No item to update', str(response.json))

    def test_food_resource_edit(self):
        response = self.client.put('api/v2/meals/1', json=self.meals[2],
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        
    def test_food_resource_delete(self):
        response = self.client.delete('api/v2/meals/1', headers=self.admin_headers)
        self.assertEqual(response.status_code, 202)

    def test_food_resource_delete_non_existent(self):
        response = self.client.delete('api/v2/meals/56', headers=self.admin_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('not exist', str(response.json))

    def test_food_resource_add_empty(self):
        response = self.client.post('api/v2/menu', json=self.meals[1],
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required', str(response.json['message']))
        
if __name__ == "__main__":
    unittest.main()