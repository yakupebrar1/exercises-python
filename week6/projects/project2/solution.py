# Project 2 — Number Guessing Game
# Author: Ebrar
# Date: April 13, 2026

import random

# Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

# Set up a guesses counter
attempts = 0
guess = 0

print("I'm thinking of a number between 1 and 10. Can you guess it?")

# While loop — keep asking until the guess is correct
while guess != secret_number:
    try:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1  # Count each guess

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")

    except ValueError:
        print("Please enter a valid whole number.")

# Print the congratulations message with the number of guesses
print(f"Congratulations! You guessed it in {attempts} attempts.")
