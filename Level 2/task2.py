#level2 task2 a advanced number guessing game
import random

def number_guessing_game():
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    secret_number = random.randint(lower_bound, upper_bound)

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < lower_bound or guess > upper_bound:
                print("Your guess is out of range. Try again.")
            elif guess > secret_number:
                print("Too high!")
            elif guess < secret_number:
                print("Too low!")
            else:
                print("You got it! Congratulations!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the game
number_guessing_game()
