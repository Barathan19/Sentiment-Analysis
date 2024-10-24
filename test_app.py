import unittest
import json
from app import app  # Make sure to import your Flask app correctly

class SentimentAnalysisAppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        """Test if the index page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sentiment Analysis VADER Sentiment', response.data)

    def test_sentiment_analysis_positive(self):
        """Test the sentiment analysis with a positive text."""
        response = self.app.post('/', data={'text1': 'I love this product!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The sentiment of: "I love this product!" is', response.data)

    def test_sentiment_analysis_negative(self):
        """Test the sentiment analysis with a negative text."""
        response = self.app.post('/', data={'text1': 'I hate this service!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The sentiment of: "I hate this service!" is', response.data)

    def test_sentiment_analysis_neutral(self):
        """Test the sentiment analysis with a neutral text."""
        response = self.app.post('/', data={'text1': 'This is a book.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The sentiment of: "This is a book." is', response.data)

    def test_invalid_input(self):
        """Test the sentiment analysis with invalid input (empty text)."""
        response = self.app.post('/', data={'text1': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your text here...', response.data)

if __name__ == '__main__':
    unittest.main()
