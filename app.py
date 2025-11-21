"""Smart Study Companion - Main Application File

This is the entry point for the Smart Study Companion application.
It initializes the Flask app and configures all routes and services.
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from models.summarizer import TextSummarizer

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///study_companion.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
CORS(app)
db = SQLAlchemy(app)

# Import routes (will be created later)
# from api import auth, study

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    """API health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Smart Study Companion API is running'
    })

@app.route('/api/v1/summarize', methods=['POST'])
def summarize_text():
    """Endpoint to summarize text using AI"""
    data = request.json
    text = data.get('text', '')
    
    
    if not text or len(text.strip()) == 0:
        return jsonify({'error': 'Text cannot be empty'}), 400
    
    # Get optional parameters
    max_length = data.get('max_length', 150)
    summary_type = data.get('summary_type', 'concise')
    
    try:
        # Initialize summarizer
        summarizer = TextSummarizer()
        
        # Perform summarization
        result = summarizer.summarize(text, max_length=max_length, summary_type=summary_type)
        
        return jsonify({
            'success': True,
            'summary': result['summary'],
            'original_length': result['original_length'],
            'summary_length': result['summary_length'],
            'compression_ratio': result['compression_ratio'],
            'word_count': result['word_count']
        })
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Summarization failed: {str(e)}'}), 500
    
@app.route('/api/v1/recommendations', methods=['POST'])
def get_recommendations():
    """Endpoint to get study recommendations"""
    data = request.json
    subject = data.get('subject', '')
    level = data.get('level', 'beginner')
    
    # TODO: Implement recommendation engine
    return jsonify({
        'recommendations': [],
        'message': 'Recommendation engine coming soon!'
    })

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Run the application
    debug_mode = os.getenv('FLASK_DEBUG', 'True') == 'True'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
