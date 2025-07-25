#!/usr/bin/env python3

"""Mini Chatbot.

The mini chatbot that interacts with the user, asking for their name and age,
and providing a personalized greeting. The chatbot is designed to be straightforward and
interactive, allowing users to practice basic programming concepts such as input
handling and string manipulation.

After the user inputs their name and age, the chatbot will respond with a greeting
and a message that includes the user's name and age.
The chatbot also includes basic questions to engage the user in a simple conversation.
"""

import random

word_bank = ["valuable", "fun", "creative", "challenging", "rewarding"]
lang_responses = [
    "{lang} is a great choice!",
    "I've heard a lot about {lang}.",
    "{lang}? Nice! Many people love it.",
    "{lang} is popular among developers.",
    "Cool! {lang} can do amazing things.",
]
hobby_responses = [
    "That sounds fun! I wish I could try {hobby} too.",
    "{hobby} is a great way to spend your time!",
    "I've read that {hobby} is very enjoyable.",
    "{hobby}? Awesome!",
    "Everyone needs a hobby! {hobby} sounds interesting.",
]
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do Java developers wear glasses? Because they don't see sharp!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why was the computer cold? It forgot to close its Windows!",
]


def get_user_name() -> str:
    """Prompt the user for their name until a valid input is provided.

    The function will keep asking for input until the user provides a non-empty string.
    It trims any leading or trailing whitespace from the input.

    Returns:
        str: The user's name, stripped of whitespace.
    """
    while True:
        name = input("What's your name? ")
        if name.strip():
            return name.strip()
        else:
            print("Please enter a valid name.")


def get_user_age() -> int:
    """Prompt the user for their age until a valid input is provided.

    Returns:
        int: The user's age as a positive integer.
    """
    while True:
        age_input = input("How old are you? ")
        try:
            age = int(age_input)
            if age > 0:
                return age
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("That's not a valid age. Please enter a number.")


def ask_basic_question():
    """Ask a basic question about programming preferences.

    Returns:
        str: The user's response to the programming question.
    """
    print("Do you like programming?")
    answer = input("(yes/no): ").strip().lower()
    if answer.startswith("y"):
        print(
            f"That's awesome! Programming is a {random.choice(word_bank)} skill."
        )
        ask_favorite_language()
    elif answer.startswith("n"):
        print("That's okay! There are many other interesting things to do.")
    else:
        print("I didn't understand your answer, but let's continue!")
    return answer


def ask_favorite_language():
    """Ask about the user's favorite programming language."""
    lang = input("What's your favorite programming language? ").strip()
    if lang:
        print(random.choice(lang_responses).format(lang=lang))
    else:
        print("No favorite? That's okay!")


def ask_hobby():
    """Ask about the user's hobby."""
    hobby = input("What do you like to do in your free time? ").strip()
    if hobby:
        print(random.choice(hobby_responses).format(hobby=hobby))
    else:
        print("Everyone needs a hobby! Maybe you'll find one soon.")


def ask_joke():
    print("Would you like to hear a joke?")
    answer = input("(yes/no): ").strip().lower()
    if answer.startswith("y"):
        print(random.choice(jokes))
    else:
        print("No worries! Maybe next time.")


def main():
    print("Hello! I am your mini chatbot.")
    name = get_user_name()
    age = get_user_age()
    print(f"Nice to meet you, {name.title()}! You are {age} years old.")
    ask_basic_question()
    ask_hobby()
    ask_joke()
    print("It was nice chatting with you. Goodbye!")


if __name__ == "__main__":
    main()
