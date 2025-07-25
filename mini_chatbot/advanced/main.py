#!/usr/bin/env python3

# type: ignore

"""Advanced Mini Chatbot with Google Gemini AI Integration.

This advanced chatbot uses Google's Gemini AI model to provide intelligent responses
to user queries. It maintains conversation context and provides a more natural
chat experience compared to the basic rule-based chatbot.

Features:
- Real AI-powered responses using Google's Gemini API
- Conversation history tracking
- Customizable personality and behavior
- Error handling and fallback responses
- User-friendly interface with typing indicators

Requirements:
- google-generativeai library (install with: pip install google-generativeai)
- Valid Google AI API key

Usage:
    python advanced.py
"""

import os
import sys
import time
import json
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

# Try to load environment variables from .env file
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # dotenv is optional, will fall back to regular environment variables
    pass

try:
    import google.generativeai as genai
except ImportError:
    print(
        "Google Generative AI library not found. Please install it with: pip install google-generativeai"
    )
    sys.exit(1)


@dataclass
class ChatMessage:
    """Represents a single chat message."""

    role: str  # 'user', 'assistant', or 'system'
    content: str
    timestamp: Optional[datetime] = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()


class AdvancedChatbot:
    """Advanced chatbot powered by Google's Gemini AI model."""

    def __init__(
        self, api_key: Optional[str] = None, model: str = "gemini-1.5-flash"
    ):
        """Initialize the chatbot.

        Args:
            api_key: Google AI API key. If None, will try to get from environment.
            model: The Gemini model to use for responses.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model
        self.conversation_history: List[ChatMessage] = []
        self.chat_session = None

        # System prompt to define the chatbot's personality
        self.system_prompt = """You are a friendly, helpful, and engaging chatbot assistant.
        You have a warm personality and enjoy having conversations with users.
        You're knowledgeable about a wide range of topics but keep your responses concise and conversational.
        If you don't know something, you're honest about it.
        You remember context from the conversation and can refer back to previous messages."""

        self._initialize_client()
        self._start_chat_session()

    def _initialize_client(self):
        """Initialize the Google AI client."""
        if not self.api_key:
            print("❌ Error: Google AI API key not found!")
            print("Please set your API key in one of these ways:")
            print("1. Set the GEMINI_API_KEY environment variable")
            print("2. Pass the API key when creating the chatbot")
            print(
                "\nYou can get an API key from: https://makersuite.google.com/app/apikey"
            )
            sys.exit(1)

        try:
            genai.configure(api_key=self.api_key)
            # Test the connection by listing models
            list(genai.list_models())
            print("✅ Successfully connected to Google AI API")
        except Exception as e:
            print(f"❌ Error connecting to Google AI API: {e}")
            print("Please check your API key and internet connection.")
            sys.exit(1)

    def _start_chat_session(self):
        """Start a new chat session with the model."""
        try:
            model = genai.GenerativeModel(
                model_name=self.model, system_instruction=self.system_prompt
            )
            self.chat_session = model.start_chat(history=[])

            # Add system message to our internal history
            system_message = ChatMessage(
                role="system", content=self.system_prompt
            )
            self.conversation_history.append(system_message)

        except Exception as e:
            print(f"❌ Error starting chat session: {e}")
            sys.exit(1)

    def _typing_indicator(self, duration: float = 1.5):
        """Show a typing indicator to simulate natural conversation flow."""
        print("🤖 Thinking", end="", flush=True)
        for _ in range(int(duration * 3)):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()

    def get_ai_response(self, user_message: str) -> str:
        """Get AI response from Google Gemini API.

        Args:
            user_message: The user's message to respond to.

        Returns:
            AI-generated response string.
        """
        # Add user message to history
        user_msg = ChatMessage(role="user", content=user_message)
        self.conversation_history.append(user_msg)

        try:
            # Show typing indicator
            self._typing_indicator()

            # Send message to Gemini
            response = self.chat_session.send_message(user_message)
            ai_response = response.text

            # Add AI response to history
            ai_msg = ChatMessage(role="assistant", content=ai_response)
            self.conversation_history.append(ai_msg)

            return ai_response

        except Exception as e:
            error_message = str(e).lower()
            if "quota" in error_message or "limit" in error_message:
                return "I'm getting too many requests right now. Please wait a moment and try again."
            elif "api" in error_message:
                return f"I'm having trouble connecting to my brain right now. Error: {e}"
            else:
                return f"Something unexpected happened: {e}"

    def get_conversation_summary(self) -> str:
        """Get a summary of the conversation so far."""
        if len(self.conversation_history) <= 1:  # Only system message
            return "No conversation yet."

        user_messages = [
            msg for msg in self.conversation_history if msg.role == "user"
        ]
        ai_messages = [
            msg for msg in self.conversation_history if msg.role == "assistant"
        ]

        return f"Conversation stats: {len(user_messages)} user messages, {len(ai_messages)} AI responses"

    def save_conversation(self, filename: Optional[str] = None):
        """Save the conversation to a JSON file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chatbot_conversation_{timestamp}.json"

        conversation_data = []
        for msg in self.conversation_history:
            if msg.role != "system":  # Don't save system messages
                conversation_data.append(
                    {
                        "role": msg.role,
                        "content": msg.content,
                        "timestamp": (
                            msg.timestamp.isoformat()
                            if msg.timestamp
                            else datetime.now().isoformat()
                        ),
                    }
                )

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(conversation_data, f, indent=2, ensure_ascii=False)
            print(f"💾 Conversation saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving conversation: {e}")

    def clear_history(self):
        """Clear conversation history and start a new chat session."""
        self.conversation_history = []
        self._start_chat_session()
        print("🗑️ Conversation history cleared.")


def print_welcome_message():
    """Print the welcome message with instructions."""
    print("🤖 " + "=" * 60)
    print("    Welcome to the Advanced AI Chatbot!")
    print("=" * 64)
    print()
    print("✨ Features:")
    print("   • Powered by Google's Gemini AI model")
    print("   • Natural conversation with memory")
    print("   • Type 'help' for commands")
    print("   • Type 'quit' or 'exit' to leave")
    print()
    print("💬 Start chatting below:")
    print("-" * 64)


def print_help():
    """Print available commands."""
    print()
    print("🔧 Available Commands:")
    print("   help        - Show this help message")
    print("   clear       - Clear conversation history")
    print("   summary     - Show conversation summary")
    print("   save        - Save conversation to file")
    print("   quit/exit   - Exit the chatbot")
    print()


def print_typing_animation(text: str, delay: float = 0.01):
    """Print text with a typing animation effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def main():
    """Main chatbot application."""
    print_welcome_message()

    # Initialize the chatbot
    try:
        chatbot = AdvancedChatbot()
    except KeyboardInterrupt:
        print("👋 Goodbye!")
        return

    print("🎯 Chatbot initialized successfully!")
    print(
        "💡 Tip: Try asking me about anything - I can help with various topics!"
    )
    print()

    # Main conversation loop
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()

            # Handle empty input
            if not user_input:
                continue

            # Handle commands
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("🤖 Thanks for chatting! Have a great day! 👋")
                break
            elif user_input.lower() == "help":
                print_help()
                continue
            elif user_input.lower() == "clear":
                chatbot.clear_history()
                continue
            elif user_input.lower() == "summary":
                print(f"📊 {chatbot.get_conversation_summary()}")
                continue
            elif user_input.lower() == "save":
                chatbot.save_conversation()
                continue

            # Get AI response
            response = chatbot.get_ai_response(user_input)
            print("🤖", end=" ")
            print_typing_animation(response)

        except KeyboardInterrupt:
            print("🤖 Chat interrupted. Thanks for chatting! 👋")
            break
        except EOFError:
            print("🤖 Input ended. Goodbye! 👋")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            print("Please try again or type 'quit' to exit.")


if __name__ == "__main__":
    main()
