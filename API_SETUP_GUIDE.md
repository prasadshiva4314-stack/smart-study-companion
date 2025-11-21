# 🔑 API Setup Guide - OpenAI API Key

## ⚠️ IMPORTANT: You MUST Create a NEW API Key

**This project requires a FRESH OpenAI API key that you create specifically for this application.** Do NOT reuse old keys from other projects.

## 📝 Step-by-Step Guide to Get a NEW OpenAI API Key

### Step 1: Create/Login to OpenAI Account

1. Go to [https://platform.openai.com/signup](https://platform.openai.com/signup)
2. Create a new account OR login to your existing account
3. You'll need to verify your email address

### Step 2: Add Payment Method (Required)

⚠️ **OpenAI requires a valid payment method to generate API keys**

1. Go to [https://platform.openai.com/account/billing/overview](https://platform.openai.com/account/billing/overview)
2. Click "Add payment method"
3. Enter your credit/debit card details
4. Add a minimum balance (recommended: $5-$10 to start)

### Step 3: Create a NEW API Key

1. Navigate to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click the **"+ Create new secret key"** button
3. Give your key a name: `Smart-Study-Companion-2025`
4. **IMPORTANT**: Copy the API key immediately - you won't be able to see it again!
5. The key will look like: `sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Step 4: Save Your API Key Securely

**⚠️ NEVER share your API key publicly or commit it to GitHub!**

1. Create a `.env` file in your project root directory:
   ```bash
   touch .env
   ```

2. Open the `.env` file and add your NEW API key:
   ```env
   OPENAI_API_KEY=sk-proj-your_actual_key_here
   DATABASE_URL=sqlite:///study_companion.db
   SECRET_KEY=your_secret_key_here_generate_random
   FLASK_DEBUG=True
   ```

3. Make sure `.env` is in your `.gitignore` file (it already is!)

## 💰 OpenAI API Pricing (Pay-as-you-go)

### GPT-3.5 Turbo (Recommended for development)
- **Input**: $0.0005 per 1K tokens (~$0.50 per 1M tokens)
- **Output**: $0.0015 per 1K tokens (~$1.50 per 1M tokens)
- **Good for**: Testing and development

### GPT-4 Turbo (For production)
- **Input**: $0.01 per 1K tokens  
- **Output**: $0.03 per 1K tokens
- **Better quality** but more expensive

### Cost Estimate for Students:
- **Light usage** (100 requests/day): ~$1-2/month
- **Medium usage** (500 requests/day): ~$5-10/month
- **Heavy usage** (1000+ requests/day): ~$15-30/month

## 🛡️ Security Best Practices

### ✅ DO:
- Create a NEW key for each project
- Store keys in `.env` files (never in code)
- Set usage limits on your OpenAI dashboard
- Monitor your usage regularly
- Rotate keys periodically (every 3-6 months)
- Delete old unused keys

### ❌ DON'T:
- Share your API key with anyone
- Commit API keys to Git/GitHub
- Use the same key across multiple projects
- Leave keys in code comments
- Post keys in forums or chat groups
- Reuse old API keys from previous projects

## 🔒 Set Usage Limits (Recommended)

1. Go to [https://platform.openai.com/account/limits](https://platform.openai.com/account/limits)
2. Set a **monthly budget limit** (e.g., $10/month)
3. Set **usage notifications** at 50%, 75%, and 90%
4. This protects you from unexpected charges!

## 🧪 Test Your API Key

Once you've added your key to `.env`, test it:

```bash
python
```

Then in Python:
```python
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Test the API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say 'API key works!'"}]
)

print(response.choices[0].message.content)
```

If you see "API key works!", you're all set! 🎉

## 🆓 Free Alternatives (if you don't want to pay)

If you don't want to use OpenAI, here are free alternatives:

1. **Hugging Face API** (Free tier available)
   - [https://huggingface.co/inference-api](https://huggingface.co/inference-api)
   - Free models available

2. **Cohere API** (Free tier)
   - [https://cohere.com](https://cohere.com)
   - Free tier: 100 requests/month

3. **Google PaLM API**
   - [https://makersuite.google.com](https://makersuite.google.com)
   - Free tier available

## 📞 Need Help?

- **OpenAI Documentation**: [https://platform.openai.com/docs](https://platform.openai.com/docs)
- **OpenAI Community**: [https://community.openai.com](https://community.openai.com)
- **Project Issues**: [Open an issue on GitHub](https://github.com/prasadshiva4314-stack/smart-study-companion/issues)

---

**Remember**: Always create a NEW API key for this project. Never reuse old keys! 🔐
