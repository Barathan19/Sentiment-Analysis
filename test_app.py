import unittest
import json
from app import app  # Make sure to import your Flask app correctly

class SentimentAnalysisAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_sentiment_analysis_positive(self):
        response = self.app.post('/', data={'text1': 'I love this product!'})
        self.assertIn(b'The sentiment of: "I love this product!" is', response.data)
        self.assertIn(b'Positive', response.data)

    def test_sentiment_analysis_negative(self):
        response = self.app.post('/', data={'text1': 'I hate this service!'})
        self.assertIn(b'The sentiment of: "I hate this service!" is', response.data)
        self.assertIn(b'Negative', response.data)

    def test_sentiment_analysis_neutral(self):
        response = self.app.post('/', data={'text1': 'This is a book.'})
        self.assertIn(b'The sentiment of: "This is a book." is', response.data)
        self.assertIn(b'Neutral', response.data)

    def test_invalid_input(self):
        """Test the sentiment analysis with invalid input (empty text)."""
        response = self.app.post('/', data={'text1': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your text here...', response.data)

if __name__ == '__main__':
    unittest.main()
