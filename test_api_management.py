import unittest
from flask import Flask
from api_management import app

class TestAPIManagement(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_analyze_emotion_endpoint(self):
        response = self.app.post('/analyze_emotion', json={'text': 'I am very happy today!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('emotion', response.json)

    def test_generate_music_endpoint(self):
        response = self.app.post('/generate_music', json={'description': 'A happy tune', 'duration': 5})
        self.assertEqual(response.status_code, 200)
        self.assertIn('music', response.json)

if __name__ == '__main__':
    unittest.main() 