import unittest
from django.test import Client
from decouple import config

class AuthViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    # Login
    def test_login_right_credentials(self):
        response = self.client.post('/login/', {'username': config('ADMIN_USERNAME'), 'password': config('ADMIN_PASSWORD')})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful', response.content.decode())

    def test_login_wrong_credentials(self):
        response = self.client.post('/login/', {'username': 'wrongname', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid credentials', response.content.decode())
    
    def test_login_wrong_method(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid request method', response.content.decode())

    # Logout
    # def test_logout_view(self):
    #     self.client.login(username='testuser', password='testpass')
    #     response = self.client.get('/logout/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Logout successful', response.content.decode())

if __name__ == '__main__':
    unittest.main()