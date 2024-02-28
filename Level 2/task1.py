#task1 number guesing game 
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    guesses = 0

    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1

            if guess > secret_number:
                print("Too high!")
            elif guess < secret_number:
                print("Too low!")
            else:
                print(f"You got it! It took you {guesses} guesses.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the game
guessing_game()
