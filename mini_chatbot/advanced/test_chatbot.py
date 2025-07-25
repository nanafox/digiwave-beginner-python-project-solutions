#!/usr/bin/env python3

# type: ignore

"""Test script for the Gemini-powered chatbot."""

import os


def test_chatbot():
    """Test the chatbot functionality."""
    print("🧪 Testing Gemini Chatbot...")
    print("=" * 40)

    # Check if API key is set
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ No GEMINI_API_KEY found in environment")
        print("💡 Please set your API key in .env file or environment")
        return False

    print("✅ API key found")

    # Try importing dependencies
    try:
        import google.generativeai as genai

        print("✅ Google AI library imported successfully")
    except ImportError:
        print("❌ Google AI library not found")
        print("💡 Run: pip install google-generativeai")
        return False

    # Test API connection
    try:
        genai.configure(api_key=api_key)
        models = list(genai.list_models())
        print(f"✅ API connection successful ({len(models)} models available)")
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        return False

    # Test chatbot initialization
    try:
        from main import AdvancedChatbot

        chatbot = AdvancedChatbot()
        print("✅ Chatbot initialized successfully")
    except Exception as e:
        print(f"❌ Chatbot initialization failed: {e}")
        return False

    # Test simple conversation
    try:
        response = chatbot.get_ai_response(
            "Hello! Can you briefly introduce yourself?"
        )
        print(f"✅ AI Response received: {response[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Chat test failed: {e}")
        return False


if __name__ == "__main__":
    # Load environment variables
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass

    success = test_chatbot()

    if success:
        print("\n🎉 All tests passed! Your chatbot is ready to use.")
        print("💡 Run: python main.py")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        print("💡 Try running: python setup.py")
