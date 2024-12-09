import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    
    # Generate a random number
    target_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
import random
