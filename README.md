# 🎓 Smart Study Companion

> AI-powered learning assistant that helps students with personalized study recommendations, content summarization, and progress tracking.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow)](https://github.com/prasadshiva4314-stack/smart-study-companion)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

## 🌟 Overview

learn. It provides personalized study recommendations, intelligent content summarization, and comprehensive progress tracking to help students achieve their academic goals more efficiently.

### Why Smart Study Companion?

- **Personalized Learning**: Adaptive recommendations based on individual learning patterns
- **Time-Efficient**: Quick summaries of lengthy study materials
- **Progress Tracking**: Visual analytics to monitor your learning journey
- **AI-Powered**: Leverages machine learning for intelligent insights

## ✨ Features

### Current Features
- 📚 **Content Summarization**: Automatically summarize long texts, articles, and documents
- 🎯 **Study Recommendations**: Get personalized study material suggestions
- 📊 **Progress Dashboard**: Track your learning progress with visual analytics
- 🤖 **AI Chat Assistant**: Ask questions and get instant answers

### Planned Features
- 🔔 Study reminders and scheduling
- 📝 Note-taking with AI organization
- 🎮 Gamification elements (badges, streaks, achievements)
- 👥 Collaborative study groups
- 📱 Mobile app support

## 🛠 Tech Stack

- **Backend**: Python, Flask/FastAPI
- **AI/ML**: OpenAI API, Hugging Face Transformers, LangChain
- **Database**: SQLite/PostgreSQL
- **Frontend**: React.js (planned)
- **Deployment**: Docker, Heroku/AWS

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/prasadshiva4314-stack/smart-study-companion.git
cd smart-study-companion
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///study_companion.db
SECRET_KEY=your_secret_key_here
```

### Step 5: Initialize Database
```bash
python init_db.py
```

### Step 6: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🚀 Usage

### Basic Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Access the web interface**: Open your browser and navigate to `http://localhost:5000`

3. **Create an account**: Sign up with your email and password

4. **Start learning**: Upload study materials or ask questions to the AI assistant

### API Usage (for developers)

```python
import requests

# Summarize text
response = requests.post('http://localhost:5000/api/summarize', 
    json={'text': 'Your long text here'})
print(response.json()['summary'])

# Get study recommendations
response = requests.post('http://localhost:5000/api/recommendations',
    json={'subject': 'mathematics', 'level': 'intermediate'})
print(response.json()['recommendations'])
```

## 📁 Project Structure

```
smart-study-companion/
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore file
├── README.md              # This file
├── models/                # AI models and ML logic
│   ├── summarizer.py
│   ├── recommender.py
│   └── chatbot.py
├── api/                   # API routes
│   ├── __init__.py
│   ├── auth.py
│   └── study.py
├── database/              # Database models and migrations
│   ├── models.py
│   └── db.py
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # HTML templates
│   ├── index.html
│   └── dashboard.html
├── tests/                 # Unit and integration tests
│   ├── test_api.py
│   └── test_models.py
└── utils/                 # Utility functions
    ├── helpers.py
    └── validators.py
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Write unit tests for new features
- Update documentation as needed
- Keep commits clean and descriptive

## 🗺 Roadmap

### Phase 1: Core Features (Current)
- [x] Project setup and repository creation
- [ ] Basic content summarization
- [ ] User authentication
- [ ] Progress tracking system

### Phase 2: AI Enhancement
- [ ] Advanced NLP capabilities
- [ ] Personalized recommendation engine
- [ ] Interactive chatbot

### Phase 3: Expansion
- [ ] Mobile application
- [ ] Collaborative features
- [ ] Integration with educational platforms
- [ ] Gamification system


## 👤 Author

**Prasad Shiva**
- GitHub: [@prasadshiva4314-stack](https://github.com/prasadshiva4314-stack)
- Kaggle: [Smart Study Companion Project](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/smart-study-companion-ai-powered-learning-assista)

## 🙏 Acknowledgments

- OpenAI for GPT API
- Hugging Face for transformer models
- The open-source community

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Check the [documentation](https://github.com/prasadshiva4314-stack/smart-study-companion/wiki)

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!

**Made with ❤️ for students worldwide**
