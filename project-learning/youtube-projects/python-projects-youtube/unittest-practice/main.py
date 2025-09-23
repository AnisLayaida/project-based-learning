import requests
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock

def get_user_data(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json()

class TestUserData(TestCase):
    @patch('requests.get')
    def test_get_user_data(self, mock_get_response):
        mock_response = Mock()
        response_dict = {
            "id",
            "name",
            "username",
            "email"
}
        mock_response.json.return_value = response_dict

        mock_get_response.return_value = mock_response

        user_data = get_user_data(1)

        mock_get_response.assert_called_with("https://jsonplaceholder.typicode.com/users/1")
        self.assertEqual(user_data, response_dict)

if __name__ == '__main__':
    unittest.main()

