"""Text Summarization Module

This module provides AI-powered text summarization functionality
using OpenAI's GPT API and Hugging Face transformers.
"""

import os
from typing import Dict, Optional
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document


class TextSummarizer:
    """AI-powered text summarization class
    
    This class handles text summarization using OpenAI's GPT models
    with support for long documents through chunking and chaining.
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        """Initialize the TextSummarizer
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: OpenAI model to use (default: gpt-3.5-turbo)
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
        
        openai.api_key = self.api_key
        self.model = model
        self.llm = ChatOpenAI(temperature=0, model_name=model, openai_api_key=self.api_key)
        
    def summarize(self, text: str, max_length: int = 150, summary_type: str = "concise") -> Dict:
        """Summarize the given text
        
        Args:
            text: The text to summarize
            max_length: Maximum length of summary in words
            summary_type: Type of summary ('concise', 'detailed', 'bullet_points')
            
        Returns:
            Dictionary containing:
                - summary: The summarized text
                - original_length: Character count of original text
                - summary_length: Character count of summary
                - compression_ratio: Ratio of summary to original length
        """
        if not text or len(text.strip()) == 0:
            raise ValueError("Text cannot be empty")
        
        try:
            # For short texts (< 1000 chars), use direct API call
            if len(text) < 1000:
                summary = self._summarize_short(text, summary_type, max_length)
            else:
                # For long texts, use LangChain with chunking
                summary = self._summarize_long(text, summary_type, max_length)
            
            return {
                'summary': summary,
                'original_length': len(text),
                'summary_length': len(summary),
                'compression_ratio': round(len(summary) / len(text), 2),
                'word_count': len(summary.split())
            }
            
        except openai.error.AuthenticationError:
            raise ValueError("Invalid OpenAI API key")
        except openai.error.RateLimitError:
            raise ValueError("OpenAI API rate limit exceeded. Please try again later.")
        except Exception as e:
            raise Exception(f"Summarization failed: {str(e)}")
    
    def _summarize_short(self, text: str, summary_type: str, max_length: int) -> str:
        """Summarize short text using direct OpenAI API call"""
        prompt = self._build_prompt(text, summary_type, max_length)
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates concise and accurate summaries."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_length * 2,  # Approximate tokens
            temperature=0.3
        )
        
        return response.choices[0].message['content'].strip()
    
    def _summarize_long(self, text: str, summary_type: str, max_length: int) -> str:
        """Summarize long text using LangChain with chunking"""
        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        
        # Create documents
        chunks = text_splitter.split_text(text)
        docs = [Document(page_content=chunk) for chunk in chunks]
        
        # Use map_reduce chain for summarization
        chain = load_summarize_chain(
            self.llm,
            chain_type="map_reduce",
            verbose=False
        )
        
        summary = chain.run(docs)
        
        # Apply summary type formatting
        if summary_type == "bullet_points":
            summary = self._format_as_bullets(summary)
        
        return summary
    
    def _build_prompt(self, text: str, summary_type: str, max_length: int) -> str:
        """Build the summarization prompt based on type"""
        base_prompt = f"Please summarize the following text in approximately {max_length} words."
        
        if summary_type == "concise":
            instruction = "Provide a concise summary capturing the main points."
        elif summary_type == "detailed":
            instruction = "Provide a detailed summary including key details and supporting information."
        elif summary_type == "bullet_points":
            instruction = "Provide a summary in bullet point format, highlighting key points."
        else:
            instruction = "Provide a clear summary."
        
        return f"{base_prompt}\n{instruction}\n\nText:\n{text}\n\nSummary:"
    
    def _format_as_bullets(self, text: str) -> str:
        """Format text as bullet points if not already formatted"""
        if '•' in text or '-' in text:
            return text
        
        sentences = text.split('. ')
        bullets = ['• ' + sent.strip() + ('.' if not sent.endswith('.') else '') for sent in sentences if sent.strip()]
        return '\n'.join(bullets)
    
    def batch_summarize(self, texts: list, **kwargs) -> list:
        """Summarize multiple texts in batch
        
        Args:
            texts: List of texts to summarize
            **kwargs: Additional arguments passed to summarize()
            
        Returns:
            List of summary dictionaries
        """
        summaries = []
        for text in texts:
            try:
                summary = self.summarize(text, **kwargs)
                summaries.append(summary)
            except Exception as e:
                summaries.append({
                    'error': str(e),
                    'original_text': text[:100] + '...' if len(text) > 100 else text
                })
        return summaries
