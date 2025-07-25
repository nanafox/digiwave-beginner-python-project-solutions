#!/usr/bin/env python3

"""Number Guessing Game.

The number guessing game where the player has to guess a number between 1 and 100.
The player has 3 attempts to guess the number correctly.
The idea of the game is to provide a fun and interactive way to practice basic programming concepts.
"""

import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    attempts = 3 # Number of attempts allowed
    guess_found = False

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            attempts -= 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                guess_found = True
                break
        except ValueError:
            print("Please enter a valid integer.")

    if not guess_found:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()