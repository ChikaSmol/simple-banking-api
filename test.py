import unittest
import json

from main import app

class TestBankApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        # Test creating a new user
        data = {'username': 'test_user'}
        response = self.app.post('/create_user', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('user', data)

    def test_get_user(self):
        # Test getting user details
        response = self.app.get('/get_user/test_user')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('user', data)

    def test_deposit(self):
        # Test depositing funds
        data = {'username': 'test_user', 'amount': 100}
        response = self.app.post('/deposit', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('balance', data)

    def test_withdraw(self):
        # Test withdrawing funds
        data = {'username': 'test_user', 'amount': 50}
        response = self.app.post('/withdraw', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('balance', data)

    def test_get_balance(self):
        # Test getting account balance
        response = self.app.get('/get_balance/test_user')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('balance', data)

    def test_send_funds(self):
        # Create test users
        create_user_data = {'username': 'test_user1'}
        self.app.post('/create_user', json=create_user_data)
        create_user_data = {'username': 'test_user2'}
        self.app.post('/create_user', json=create_user_data)

        # Deposit funds to test_user1
        deposit_data = {'username': 'test_user1', 'amount': 100}
        self.app.post('/deposit', json=deposit_data)

        # Send funds from test_user1 to test_user2
        send_funds_data = {'sender': 'test_user1', 'receiver': 'test_user2', 'amount': 30}
        response = self.app.post('/send_funds', json=send_funds_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('sender_balance', data)
        self.assertIn('receiver_balance', data)

if __name__ == '__main__':
    unittest.main()
