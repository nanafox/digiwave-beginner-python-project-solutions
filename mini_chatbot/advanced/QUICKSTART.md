# Quick Start Guide - Gemini AI Chatbot 🚀

## 🎯 Goal

Get your AI chatbot running in 5 minutes using Google's Gemini AI!

## 📋 Prerequisites

- Python 3.7+
- Internet connection
- Google AI API key (free tier available!)

## 🔑 Step 1: Get Your API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key (starts with "AI...")

## ⚡ Step 2: Quick Setup

```bash
# Install dependencies
pip install google-generativeai python-dotenv

# Create environment file
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run the chatbot
python advanced.py
```

## 🛠️ Step 3: Alternative Setup (Guided)

```bash
# Run the automated setup
python setup.py
```

## 🎮 Step 4: Start Chatting

```text
🤖 Welcome to the Advanced AI Chatbot!
You: Hello! What can you help me with?
🤖 Thinking...
🤖 Hi there! I'm here to help with a wide variety of things...
```

## 🔧 Available Commands

- `help` - Show available commands
- `clear` - Clear conversation history
- `summary` - Show conversation stats
- `save` - Save conversation to file
- `quit` - Exit the chatbot

## 💡 Pro Tips

- Gemini has a generous free tier (15 requests/minute)
- Use `clear` to reset context and start fresh
- Conversations are automatically saved when you exit
- The chatbot remembers your entire conversation context

## 🆘 Troubleshooting

### **"Google AI library not found"**

```bash
pip install google-generativeai
```

### **"API key not found"**

- Make sure your `.env` file contains `GEMINI_API_KEY=your_key`
- Or set environment variable: `export GEMINI_API_KEY=your_key`

### **"API connection failed"**

- Check your internet connection
- Verify your API key is correct
- Make sure you're not hitting rate limits

## 🎉 You're Ready

Your AI chatbot is now powered by Google's Gemini AI. Enjoy chatting!
