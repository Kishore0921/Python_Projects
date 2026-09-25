import random

def play_game():
    # Score tracking
    user_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]

    print("=== Welcome to Rock, Paper, Scissors! ===")
    print("Type 'quit' at any time to exit the game.\n")

    # Loop for continuous gameplay
    while True:
        # User Input
        user_choice = input("Enter rock, paper, or scissors: ").lower().strip()

        if user_choice == "quit":
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        # Random computer selection
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Win / Lose / Draw detection & Game Logic
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display score tracking
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

    print("\n=== Game Over ===")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()