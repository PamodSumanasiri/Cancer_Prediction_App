import unittest
from unittest.mock import patch
from app.init import handle_login  # Replace `myapp.auth` with the actual path to your function

class TestLoginErrorHandling(unittest.TestCase):

    @patch('requests.post')  # Mock the `requests.post` method
    def test_firebase_unavailable(self, mock_post):
        # Simulate a network error (connection error)
        mock_post.side_effect = Exception("Network Unavailable")

        # Call the login function and check that it handles the error gracefully
        with self.assertRaises(Exception):  # Or catch and assert the specific message
            handle_login('test@example.com', 'validpassword')

if __name__ == '__main__':
    unittest.main()
