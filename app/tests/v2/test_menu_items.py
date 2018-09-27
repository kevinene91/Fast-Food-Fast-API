import unittest

from .base import BaseTest

class MenuTestCase(BaseTest):
    def test_menuitem_resource_add(self):
        response = self.client.post('api/v1/menuitem', json=self.menuitem[0], headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_menuitem_resource_add_existing_food(self):
        response = self.client.post('api/v1/menuitem', json=self.menuitem[0], headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('item exists',str(response.json))

    def test_menuitem_resource_add_empty(self):
        response = self.client.post('api/v1/menuitem', json=self.menuitem[1], headers=self.headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('add inputs',str(response.json))

    def test_menuitem_resource_get_specific(self):
        response = self.response = self.client.post('api/v1/menuitem/1', headers=self.headers)
        self.assertEqual(response.status_code, 200)
    
    def tes_menuitem_resource_get_all(self):
        response = self.response = self.client.post('api/v1/menuitem', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_menuitem_resource_get_non_existent(self):
        response = self.response = self.client.post('api/v1/menuitem/56', headers=self.headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('not exist',str(response.json))

    def test_menuitem_resource_edit_non_existent(self):
        response = self.client.put('api/v1/menuitem/56', json=self.menuitem[0], headers=self.headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('not exist',str(response.json))
        
    def test_menuitem_resource_delete(self):
        response = self.client.delete('api/v1/memenuitem/1', headers=self.headers)
        self.assertEqual(response.status_code, 202)

    def test_menuitem_resource_delete_non_existent(self):
        response = self.client.delete('api/v1/menuitem/56', headers=self.headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('not exist',str(response.json))