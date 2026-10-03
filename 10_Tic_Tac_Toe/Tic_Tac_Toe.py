import sys
import random

# Global Constants
VALID_SYMBOLS = ('X', 'O')
WIN_CONDITIONS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
)

def get_validated_name(prompt, existing_name=None):
    """Prompts for a non-empty name and optionally prevents duplicate names."""
    while True:
        name = input(prompt).strip()
        if not name:
            print("Name cannot be empty or contain only spaces. Please try again.")
            continue
        if existing_name and name.lower() == existing_name.lower():
            print(f"The name '{name}' is already taken. Please choose a unique name to avoid confusion.")
            continue
        return name

def print_board(board):
    """Displays the current state of the board."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, symbol):
    """Checks if the given symbol has formed any winning combinations."""
    for condition in WIN_CONDITIONS:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

def check_draw(board):
    """Checks if the board is full with no remaining empty spaces."""
    return all(space in VALID_SYMBOLS for space in board)

def play_game(player1, player2, player1_symbol, player2_symbol, round_number):
    """Runs a single round of Tic Tac Toe."""
    # Initialize board with layout numbers 1-9
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    print(f"==================================================")
    print(f"                  ===== ROUND {round_number} =====")
    print(f"==================================================")
    
    # Randomly choose who goes first
    if random.choice([True, False]):
        current_player = player1
        current_symbol = player1_symbol
    else:
        current_player = player2
        current_symbol = player2_symbol
        
    print(f"🎲 [RANDOM CHOICE] {current_player} ({current_symbol}) is selected to go first!")
    print("==================================================\n")
    
    print_board(board)

    while True:
        try:
            move_input = input(f"{current_player} ({current_symbol}), enter your move (1-9): ").strip()
            move = int(move_input) - 1
            
            if move < 0 or move > 8 or board[move] in VALID_SYMBOLS:
                print("Invalid move! That spot is either taken or out of bounds. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        # Place the symbol on the board
        board[move] = current_symbol
        print_board(board)

        # Check for Win
        if check_win(board, current_symbol):
            print(f"🎉 Congratulations {current_player}! You win Round {round_number}!")
            return current_symbol
            
        # Check for Draw
        if check_draw(board):
            print("🤝 It's a draw!")
            return "Draw"
            
        # Switch turns
        if current_symbol == player1_symbol:
            current_player = player2
            current_symbol = player2_symbol
        else:
            current_player = player1
            current_symbol = player1_symbol

def display_final_series_result(p1, p1_score, p2, p2_score):
    """Calculates and prints the ultimate series summary outcome."""
    print("\n==================================================")
    print("🏆 FINAL SERIES RESULT:")
    print(f"   {p1}: {p1_score} | {p2}: {p2_score}")
    if p1_score > p2_score:
        print(f"   🔥 Result: {p1} wins the series ({p1_score}–{p2_score})!")
    elif p2_score > p1_score:
        print(f"   🔥 Result: {p2} wins the series ({p2_score}–{p1_score})!")
    else:
        print(f"   🤝 Result: The series is tied ({p1_score}–{p2_score})!")
    print("==================================================")
    print("Thanks for playing!")

def main():
    try:
        print("Console based TIC TAC TOE game (XOX)") 
        print("""
Follow the order for gameplay:
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
""")

        # Player Setup & Name Validation
        player1 = get_validated_name("Enter player 1 name: ")
        player2 = get_validated_name("Enter player 2 name: ", existing_name=player1) 

        # Symbol Setup & Validation
        player1_symbol = input(f"{player1} choose your symbol (X or O): ").strip().upper() 
        while player1_symbol not in VALID_SYMBOLS: 
            print("Invalid symbol! Please choose either X or O.") 
            player1_symbol = input(f"{player1} choose your symbol (X or O): ").strip().upper() 

        player2_symbol = 'O' if player1_symbol == 'X' else 'X' 
        print(f"{player2} will use the symbol {player2_symbol}\n")

        # Score Tracking & Match Loop
        player1_score = 0
        player2_score = 0
        round_counter = 1

        while True:
            # Run the round and pass down required dependencies
            game_result = play_game(player1, player2, player1_symbol, player2_symbol, round_counter)
            
            # Calculate scores based on the result
            if game_result == player1_symbol:
                player1_score += 1
            elif game_result == player2_symbol:
                player2_score += 1

            # Display scorecard
            print("==================================================")
            print("📊 CURRENT SCOREBOARD:")
            print(f"   {player1}: {player1_score} | {player2}: {player2_score}")
            print("==================================================\n")

            # Rematch validation routine loop
            while True:
                restart = input("Do you want to play a rematch? (yes/no): ").strip().lower()
                if restart in ('yes', 'y'):
                    round_counter += 1
                    break
                elif restart in ('no', 'n'):
                    display_final_series_result(player1, player1_score, player2, player2_score)
                    return
                else:
                    print("Invalid response. Please type 'yes'/'y' to keep playing or 'no'/'n' to exit.")

    except (KeyboardInterrupt, EOFError):
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)

if __name__ == "__main__":
    main()
