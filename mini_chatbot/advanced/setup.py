#!/usr/bin/env python3

"""Setup script for the Advanced Mini Chatbot.

This script helps users set up the chatbot by:
1. Installing required dependencies
2. Setting up the API key
3. Testing the connection
"""

import os
import sys
import subprocess
from pathlib import Path


def install_dependencies():
    """Install required Python packages."""
    print("📦 Installing required dependencies...")

    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False


def setup_api_key():
    """Help user set up the Google AI API key."""
    print("\n🔑 Setting up Google AI API key...")

    # Check if .env file already exists
    env_file = Path(".env")
    if env_file.exists():
        print("📄 .env file already exists.")
        choice = input("Do you want to update it? (y/N): ").strip().lower()
        if choice not in ["y", "yes"]:
            return True

    # Get API key from user
    print("\n🌐 You'll need a Google AI API key to use this chatbot.")
    print("📝 Get one from: https://makersuite.google.com/app/apikey")
    print("💡 Note: Google AI has a generous free tier for Gemini models.")

    api_key = input(
        "\nEnter your Google AI API key (or press Enter to skip): "
    ).strip()

    if not api_key:
        print(
            "⏭️  API key setup skipped. You can set it later in the .env file."
        )
        return True

    # Validate API key format (basic check)
    if not api_key.startswith("AI"):
        print("⚠️  Warning: Google AI API key typically starts with 'AI'")
        choice = input("Continue anyway? (y/N): ").strip().lower()
        if choice not in ["y", "yes"]:
            return False

    # Create .env file
    try:
        with open(".env", "w") as f:
            f.write(f"GEMINI_API_KEY={api_key}\n")
            f.write("# Optional: Choose a different model\n")
            f.write("# GEMINI_MODEL=gemini-1.5-flash\n")
            f.write("# GEMINI_MODEL=gemini-1.5-pro\n")
            f.write("# GEMINI_MODEL=gemini-pro\n")

        print("✅ API key saved to .env file!")
        return True
    except Exception as e:
        print(f"❌ Error saving API key: {e}")
        return False


def test_setup():
    """Test if the setup is working."""
    print("\n🧪 Testing setup...")

    try:
        # Try importing the required modules
        import google.generativeai as genai
        from dotenv import load_dotenv

        load_dotenv()

        # Check if API key is available
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print(
                "⚠️  No API key found. The chatbot will ask for it when you run it."
            )
            return True

        # Test API connection (optional)
        print("🔗 Testing API connection...")
        genai.configure(api_key=api_key)

        # Try a simple API call
        list(genai.list_models())
        print("✅ API connection successful!")
        return True

    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"⚠️  API test failed: {e}")
        print(
            "💡 You can still use the chatbot - it will handle this error gracefully."
        )
        return True


def main():
    """Main setup function."""
    print("🤖 " + "=" * 50)
    print("   Advanced Mini Chatbot Setup (Gemini AI)")
    print("=" * 54)
    print()

    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    success = True

    # Install dependencies
    if not install_dependencies():
        success = False

    # Set up API key
    if success and not setup_api_key():
        success = False

    # Test setup
    if success:
        test_setup()

    print("\n" + "=" * 54)
    if success:
        print("🎉 Setup completed!")
        print("💡 To start the chatbot, run: python advanced.py")
    else:
        print("❌ Setup had some issues. Please check the errors above.")
        print("💡 You can try running the chatbot anyway: python advanced.py")

    print("📚 For help, check the README or comments in main.py")
    print("=" * 54)


if __name__ == "__main__":
    main()
