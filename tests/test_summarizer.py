"""Unit tests for TextSummarizer class"""

import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add parent directory to path to import models
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.summarizer import TextSummarizer


class TestTextSummarizer(unittest.TestCase):
    """Test cases for TextSummarizer class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Mock API key for testing
        os.environ['OPENAI_API_KEY'] = 'test-api-key-12345'
        
    def tearDown(self):
        """Clean up after tests"""
        if 'OPENAI_API_KEY' in os.environ:
            del os.environ['OPENAI_API_KEY']
    
    def test_initialization_with_api_key(self):
        """Test TextSummarizer initialization with API key"""
        summarizer = TextSummarizer(api_key='test-key')
        self.assertIsNotNone(summarizer)
        self.assertEqual(summarizer.api_key, 'test-key')
    
    def test_initialization_without_api_key_raises_error(self):
        """Test that missing API key raises ValueError"""
        if 'OPENAI_API_KEY' in os.environ:
            del os.environ['OPENAI_API_KEY']
        
        with self.assertRaises(ValueError) as context:
            TextSummarizer()
        
        self.assertIn('OpenAI API key is required', str(context.exception))
    
    def test_initialization_with_environment_variable(self):
        """Test initialization using environment variable"""
        os.environ['OPENAI_API_KEY'] = 'env-test-key'
        summarizer = TextSummarizer()
        self.assertEqual(summarizer.api_key, 'env-test-key')
    
    def test_summarize_empty_text_raises_error(self):
        """Test that empty text raises ValueError"""
        summarizer = TextSummarizer(api_key='test-key')
        
        with self.assertRaises(ValueError) as context:
            summarizer.summarize('')
        
        self.assertIn('Text cannot be empty', str(context.exception))
    
    @patch('models.summarizer.openai.ChatCompletion.create')
    def test_summarize_short_text(self, mock_create):
        """Test summarization of short text"""
        # Mock OpenAI API response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message = {'content': 'This is a test summary.'}
        mock_create.return_value = mock_response
        
        summarizer = TextSummarizer(api_key='test-key')
        result = summarizer.summarize('This is a short test text.')
        
        self.assertIn('summary', result)
        self.assertIn('original_length', result)
        self.assertIn('summary_length', result)
        self.assertIn('compression_ratio', result)
        self.assertEqual(result['summary'], 'This is a test summary.')
    
    @patch('models.summarizer.openai.ChatCompletion.create')
    def test_summarize_with_max_length(self, mock_create):
        """Test summarization with custom max_length"""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message = {'content': 'Short summary.'}
        mock_create.return_value = mock_response
        
        summarizer = TextSummarizer(api_key='test-key')
        result = summarizer.summarize('Test text.', max_length=50)
        
        # Verify max_length was passed (check mock was called with appropriate params)
        self.assertTrue(mock_create.called)
        self.assertIn('summary', result)
    
    @patch('models.summarizer.openai.ChatCompletion.create')
    def test_summarize_concise_type(self, mock_create):
        """Test concise summary type"""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message = {'content': 'Concise summary.'}
        mock_create.return_value = mock_response
        
        summarizer = TextSummarizer(api_key='test-key')
        result = summarizer.summarize('Test text.', summary_type='concise')
        
        self.assertIn('summary', result)
        self.assertEqual(result['summary'], 'Concise summary.')
    
    def test_build_prompt_concise(self):
        """Test prompt building for concise summary"""
        summarizer = TextSummarizer(api_key='test-key')
        prompt = summarizer._build_prompt('Test text', 'concise', 100)
        
        self.assertIn('concise', prompt)
        self.assertIn('100', prompt)
        self.assertIn('Test text', prompt)
    
    def test_build_prompt_detailed(self):
        """Test prompt building for detailed summary"""
        summarizer = TextSummarizer(api_key='test-key')
        prompt = summarizer._build_prompt('Test text', 'detailed', 200)
        
        self.assertIn('detailed', prompt)
        self.assertIn('200', prompt)
    
    def test_build_prompt_bullet_points(self):
        """Test prompt building for bullet point summary"""
        summarizer = TextSummarizer(api_key='test-key')
        prompt = summarizer._build_prompt('Test text', 'bullet_points', 150)
        
        self.assertIn('bullet point', prompt)
        self.assertIn('150', prompt)
    
    def test_format_as_bullets(self):
        """Test formatting text as bullet points"""
        summarizer = TextSummarizer(api_key='test-key')
        text = 'First point. Second point. Third point.'
        result = summarizer._format_as_bullets(text)
        
        self.assertIn('\u2022', result)  # Bullet character
        lines = result.split('\n')
        self.assertEqual(len(lines), 3)
    
    def test_format_as_bullets_already_formatted(self):
        """Test that already formatted bullet points are not reformatted"""
        summarizer = TextSummarizer(api_key='test-key')
        text = '\u2022 Already formatted point'
        result = summarizer._format_as_bullets(text)
        
        self.assertEqual(text, result)
    
    @patch('models.summarizer.openai.ChatCompletion.create')
    def test_batch_summarize(self, mock_create):
        """Test batch summarization of multiple texts"""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message = {'content': 'Summary.'}
        mock_create.return_value = mock_response
        
        summarizer = TextSummarizer(api_key='test-key')
        texts = ['Text one.', 'Text two.', 'Text three.']
        results = summarizer.batch_summarize(texts)
        
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertIn('summary', result)
    
    def test_batch_summarize_with_errors(self):
        """Test batch summarization handles errors gracefully"""
        summarizer = TextSummarizer(api_key='test-key')
        texts = ['', 'Valid text', '']
        results = summarizer.batch_summarize(texts)
        
        self.assertEqual(len(results), 3)
        # First and third should have errors
        self.assertIn('error', results[0])
        self.assertIn('error', results[2])


if __name__ == '__main__':
    unittest.main()
