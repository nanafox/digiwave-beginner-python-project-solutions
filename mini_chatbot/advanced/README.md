# Advanced Mini Chatbot 🤖

A sophisticated chatbot application powered by Google's Gemini AI that provides natural, intelligent conversations with memory and context awareness.

> **📁 Quick Navigation**: The advanced chatbot files are located in the `advanced/` directory. All commands below assume you're in that directory unless otherwise specified.

## Features ✨

- **AI-Powered Responses**: Uses Google's Gemini AI for intelligent, natural conversations
- **Conversation Memory**: Remembers context throughout the chat session
- **Interactive Commands**: Built-in commands for managing conversations
- **Conversation Saving**: Save chat history to JSON files
- **Error Handling**: Graceful handling of API errors and network issues
- **Typing Indicators**: Natural conversation flow with thinking animations
- **Customizable Personality**: Easy to modify the chatbot's behavior and responses

## Requirements 📋

- Python 3.7 or higher
- Google AI API key (free tier available!)
- Internet connection

## Quick Start 🚀

### Option 1: Automated Setup (Recommended)

1. **Run the setup script:**

   ```bash
   cd advanced
   python setup.py
   ```

   This will automatically install dependencies and help you configure your API key.

2. **Start chatting:**
   ```bash
   python main.py
   ```

### Option 2: Manual Setup

1. **Navigate to the advanced directory:**

   ```bash
   cd advanced
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**

   Create a `.env` file in the advanced directory:

   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file and add your Google AI API key:

   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. **Run the chatbot:**
   ```bash
   python main.py
   ```

## Getting a Google AI API Key 🔑

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. **Great news**: Google AI has a generous free tier for Gemini models!

## Usage 💬

Once the chatbot is running, you can:

- **Chat naturally**: Just type your messages and press Enter
- **Use commands**: Type special commands for additional features

### Available Commands

| Command          | Description                      |
| ---------------- | -------------------------------- |
| `help`           | Show available commands          |
| `clear`          | Clear conversation history       |
| `summary`        | Show conversation statistics     |
| `save`           | Save conversation to a JSON file |
| `quit` or `exit` | Exit the chatbot                 |

### Example Conversation

```
🤖 Welcome to the Advanced AI Chatbot!
You: Hello! What can you help me with?
🤖 Thinking...
🤖 Hi there! I'm here to help with a wide variety of things. I can:
- Answer questions on many topics
- Help with problem-solving
- Provide explanations and tutorials
- Have casual conversations
- Assist with creative writing
- And much more!

What would you like to talk about or get help with today?

You: Can you explain quantum computing?
🤖 Thinking...
🤖 Absolutely! Quantum computing is a fascinating field that uses the principles of quantum mechanics...
```

## Configuration ⚙️

### Environment Variables

You can customize the chatbot using these environment variables in your `.env` file:

```bash
# Required: Your Google AI API key
GEMINI_API_KEY=your_api_key_here

# Optional: Choose a different model (default: gemini-1.5-flash)
GEMINI_MODEL=gemini-1.5-flash
# GEMINI_MODEL=gemini-1.5-pro
# GEMINI_MODEL=gemini-pro
```

### Customizing the Chatbot's Personality

You can modify the `system_prompt` in the `AdvancedChatbot` class to change how the chatbot behaves:

```python
self.system_prompt = """You are a helpful assistant that specializes in programming.
You provide clear, concise code examples and explanations."""
```

## Project Structure 📁

```bash
mini_chatbot/
├── advanced/            # Advanced chatbot package
│   ├── __init__.py     # Package initialization
│   ├── main.py         # Main chatbot application (Gemini-powered)
│   ├── setup.py        # Automated setup script
│   ├── demo.py         # Interactive demo without API key
│   ├── test_chatbot.py # Test script to verify setup
│   ├── requirements.txt # Python dependencies
│   ├── README.md       # Advanced chatbot documentation
│   └── QUICKSTART.md   # Quick start guide
├── main.py             # Basic rule-based chatbot (for comparison)
├── __pycache__/        # Python cache files
└── README.md           # This file (main documentation)
```

## How It Works 🔧

1. **Initialization**: The chatbot connects to Google's Gemini AI using your API key
2. **Conversation Loop**: It waits for user input and sends it to the AI model
3. **Context Management**: Each message is stored to maintain conversation context
4. **Response Generation**: The AI generates responses based on the conversation history
5. **Error Handling**: Network issues and API errors are handled gracefully

## Troubleshooting 🔧

### Common Issues

### **"Google AI library not found"**

- Solution: Install dependencies with `pip install -r requirements.txt`

### **"Error: Google AI API key not found!"**

- Solution: Make sure your `.env` file contains a valid `GEMINI_API_KEY`

### **"Rate limit exceeded" or "Quota exceeded"**

- Solution: You're making too many requests. Wait a moment and try again.

### **"API connection fails"**

- Check your internet connection
- Verify your API key is correct
- Make sure your Google AI account is active

### Getting Help

If you encounter issues:

1. Check the error messages carefully
2. Verify your API key is correct
3. Try running `cd advanced && python setup.py` again
4. Check the [Google AI documentation](https://ai.google.dev/docs)

## Comparison with Basic Chatbot 📊

| Feature          | Basic Chatbot (`main.py`) | Advanced Chatbot (`advanced/main.py`) |
| ---------------- | ------------------------- | ------------------------------------- |
| AI Technology    | Rule-based responses      | Google Gemini AI                      |
| Responses        | Pre-programmed            | AI-generated                          |
| Memory           | None                      | Full conversation                     |
| Topics           | Limited                   | Unlimited                             |
| Learning         | No                        | Context-aware                         |
| Natural Language | Basic                     | Advanced                              |
| API Key Required | No                        | Yes (free tier available)             |

## Cost Considerations 💰

- The chatbot uses Google's Gemini AI, which has a generous free tier
- Free tier: 15 requests per minute, 1,500 requests per day
- Paid plans available for higher usage limits
- Much more cost-effective than other AI providers
- Use the `clear` command to reset context for optimal performance

## Contributing 🤝

Feel free to improve this chatbot! Some ideas:

- Add support for other AI models (Claude, OpenAI, etc.)
- Implement conversation templates
- Add voice input/output
- Create a web interface
- Add conversation analytics

## License 📄

This project is open source. Feel free to use, modify, and distribute as needed.

## Acknowledgments 🙏

- Built with [Google's Gemini AI](https://ai.google.dev/)
- Inspired by the need for accessible conversational AI tools
- Thanks to the Python community for excellent libraries

---

Happy chatting! 🎉
