#!/usr/bin/env python3

"""Demo script for the Advanced Mini Chatbot.

This script demonstrates the chatbot's capabilities without requiring
an API key by showing example conversations and features.
"""

import time


def print_typing_animation(text: str, delay: float = 0.03):
    """Print text with a typing animation effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def print_demo_header():
    """Print the demo header."""
    print("🤖 " + "=" * 60)
    print("    Advanced AI Chatbot - DEMO MODE")
    print("=" * 64)
    print()
    print(
        "🎭 This demo shows what the chatbot can do without requiring an API key."
    )
    print("💡 To use the real AI chatbot, run: python advanced.py")
    print()
    print("✨ Demo Features:")
    print("   • Example conversations")
    print("   • Feature demonstrations")
    print("   • Setup instructions")
    print()
    print("🎬 Starting demo...")
    print("-" * 64)


def demo_conversation():
    """Show a demo conversation."""
    print("\n📱 Example Conversation:")
    print("=" * 30)

    conversations = [
        ("You", "Hello! What can you help me with?"),
        (
            "🤖",
            "Hi there! I'm here to help with a wide variety of things. I can answer questions, explain concepts, help with problem-solving, assist with coding, and have engaging conversations. What would you like to explore today?",
        ),
        ("You", "Can you explain how machine learning works?"),
        (
            "🤖",
            "Absolutely! Machine learning is a subset of AI where computers learn patterns from data without being explicitly programmed for each task. Think of it like teaching a child to recognize cats - instead of describing every detail, you show them many cat photos until they learn the patterns. There are three main types: supervised learning (learning from examples), unsupervised learning (finding hidden patterns), and reinforcement learning (learning through trial and reward). Would you like me to dive deeper into any of these?",
        ),
        (
            "You",
            "That's really helpful! Can you remember what we talked about if I ask another question?",
        ),
        (
            "🤖",
            "Yes! I maintain conversation context throughout our chat session. I remember we were discussing machine learning - the three types I mentioned (supervised, unsupervised, and reinforcement learning) and the cat recognition analogy. This memory allows for more natural, flowing conversations where we can build on previous topics. What else would you like to know about ML or any other topic?",
        ),
    ]

    for speaker, message in conversations:
        if speaker == "🤖":
            print(f"\n{speaker} Thinking", end="")
            for _ in range(3):
                time.sleep(0.3)
                print(".", end="", flush=True)
            print()
            time.sleep(0.3)

        print(f"{speaker}: ", end="")
        print_typing_animation(message, 0.01)
        time.sleep(1)


def demo_commands():
    """Show available commands."""
    print("\n🔧 Available Commands:")
    print("=" * 25)

    commands = [
        ("help", "Show available commands and usage tips"),
        ("clear", "Clear conversation history to start fresh"),
        ("summary", "Display conversation statistics and summary"),
        ("save", "Save the current conversation to a JSON file"),
        ("quit/exit", "Exit the chatbot gracefully"),
    ]

    for cmd, description in commands:
        print(f"   {cmd:<12} - {description}")

    print("\n💡 Pro tip: The chatbot remembers context, so you can reference")
    print("   previous parts of your conversation naturally!")


def demo_features():
    """Demonstrate key features."""
    print("\n🌟 Key Features:")
    print("=" * 20)

    features = [
        "🧠 AI-Powered Intelligence",
        "   • Uses OpenAI's GPT models for natural, intelligent responses",
        "   • Understands context and nuance in conversations",
        "   • Can discuss virtually any topic",
        "",
        "💾 Conversation Memory",
        "   • Remembers the entire conversation context",
        "   • Can reference previous messages naturally",
        "   • Maintains coherent long-form discussions",
        "",
        "🛠️ User-Friendly Interface",
        "   • Simple command-line interface",
        "   • Typing indicators for natural feel",
        "   • Helpful error messages and guidance",
        "",
        "📁 Conversation Management",
        "   • Save conversations to JSON files",
        "   • Clear history when needed",
        "   • View conversation statistics",
        "",
        "⚡ Robust Error Handling",
        "   • Graceful handling of API issues",
        "   • Network error recovery",
        "   • Clear error messages and solutions",
    ]

    for feature in features:
        print(feature)
        time.sleep(0.3)


def demo_setup_guide():
    """Show setup instructions."""
    print("\n📋 Getting Started:")
    print("=" * 22)

    steps = [
        "1. 🔑 Get an OpenAI API Key:",
        "   • Visit: https://platform.openai.com/api-keys",
        "   • Create an account and generate an API key",
        "   • Note: Requires a paid account with credits",
        "",
        "2. 🛠️ Quick Setup:",
        "   • Run: python setup.py",
        "   • Follow the interactive setup process",
        "   • Enter your API key when prompted",
        "",
        "3. 🚀 Start Chatting:",
        "   • Run: python advanced.py",
        "   • Begin your conversation!",
        "",
        "4. 📖 Alternative Setup:",
        "   • Install dependencies: pip install -r requirements.txt",
        "   • Copy .env.example to .env",
        "   • Add your API key to the .env file",
        "   • Run: python advanced.py",
    ]

    for step in steps:
        print(step)
        time.sleep(0.2)


def demo_cost_info():
    """Show cost information."""
    print("\n💰 Cost Information:")
    print("=" * 22)

    info = [
        "The chatbot uses OpenAI's API, which charges per token:",
        "",
        "📊 Typical Costs (as of 2024):",
        "   • GPT-3.5-turbo: ~$0.0015 per 1K tokens",
        "   • GPT-4: ~$0.03 per 1K tokens",
        "   • Average conversation: $0.01 - $0.10",
        "",
        "💡 Cost-Saving Tips:",
        "   • Use 'clear' command to reset context",
        "   • Keep conversations focused",
        "   • Start with GPT-3.5-turbo (cheaper)",
        "",
        "🔍 Token Usage:",
        "   • 1 token ≈ 0.75 words",
        "   • Longer conversations use more tokens",
        "   • Context is included in each request",
    ]

    for line in info:
        print(line)
        time.sleep(0.3)


def main():
    """Run the demo."""
    print_demo_header()

    sections = [
        ("Demo Conversation", demo_conversation),
        ("Available Commands", demo_commands),
        ("Key Features", demo_features),
        ("Setup Guide", demo_setup_guide),
        ("Cost Information", demo_cost_info),
    ]

    for i, (title, demo_func) in enumerate(sections, 1):
        print(f"\n🎬 Demo {i}/5: {title}")
        time.sleep(1)
        demo_func()

        if i < len(sections):
            input("\n⏯️  Press Enter to continue to the next demo...")

    print("\n" + "=" * 64)
    print("🎉 Demo Complete!")
    print()
    print("🚀 Ready to try the real chatbot?")
    print("   1. Run: python setup.py (for guided setup)")
    print("   2. Or run: python main.py (if already configured)")
    print()
    print("📚 For more information, check out README.md")
    print("🤖 Happy chatting!")
    print("=" * 64)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Thanks for watching!")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        print("This doesn't affect the actual chatbot functionality.")
