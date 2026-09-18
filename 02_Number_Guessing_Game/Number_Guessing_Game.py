import random


def number_guessing_game():
    # 1. Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # 2. Start the game loop
    while True:
        user_input = input("Enter your guess: ")

        # 3. Validate input to make sure it's a valid integer
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")
            continue

        attempts += 1

        # 4. Check the user's guess against the secret number
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(
                f"🎉 Congratulations! You guessed the number {secret_number} correctly!"
            )
            print(f"It took you {attempts} attempts.")
            break  # Exit the loop and end the game