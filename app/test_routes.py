
import unittest
from unittest.mock import patch
from app import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_posts(self):
        
        with patch('app.routes.Post.query.all') as mock_query:
            mock_query.return_value = [{'id': 1, 'title': 'Test Post'}]
            response = self.app.get('/posts')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['title'], 'Test Post')

if __name__ == '__main__':
    unittest.main()
