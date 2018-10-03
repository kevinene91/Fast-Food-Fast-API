import unittest 

from .base import BaseTest


class AuthEndpointTestCase(BaseTest):

    def test_register_already_registered(self):
        response = self.client.post('api/v2/auth/signup', json=self.user[0])
        self.assertEqual(response.status_code, 400)
        self.assertIn('already registered', str(response.json))

    def test_register_without_data(self):
        response = self.client.post('api/v2/auth/signup', json=self.user[1])
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', str(response.json))

    def test_register_with_invalid_email(self):
        response = self.client.post('api/v2/auth/signup', json=self.user[1])
        self.assertEqual(response.status_code, 400)
    
    def test_user_login(self):
        response = self.client.post('api/v2/auth/login', json=self.user[0])
        self.assertEqual(response.status_code, 201)

    def test_user_login_without_data(self):
        response = self.client.post('api/v2/auth/login', json=self.user[1])
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', str(response.json))

    def test_login_invalid_email(self):
        response = self.client.post('api/v2/auth/login', json=self.user[3])
        self.assertEqual(response.status_code, 400)

    def test_login_invalid_password(self):
        response = self.client.post('api/v2/auth/login', json=self.user[2])
        self.assertEqual(response.status_code, 400)
      
if __name__ == "__main__":
    unittest.main()