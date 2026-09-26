# 1. DICTIONARIES: Storing quiz topics and their respective QA pairs
QUIZ_DATA = {
    1: {
        "topic": "Fruits and Vegetables",
        "questions": {
            "What fruit is known as the king of fruits?": "durian",
            "Which vegetable is known for its high vitamin A content?": "carrot",
            "What fruit is typically red and has seeds on the outside?": "strawberry"
        }
    },
    2: {
        "topic": "Animals",
        "questions": {
            "What is the largest mammal in the world?": "blue whale",
            "Which land animal can run the fastest?": "cheetah",
            "What type of animal is a komodo dragon?": "lizard"
        }
    },
    3: {
        "topic": "Countries",
        "questions": {
            "Which country has the largest population in the world?": "india",
            "What is the capital city of France?": "paris",
            "Which country is known as the Land of the Rising Sun?": "japan"
        }
    }
}

# 2. FUNCTIONS: Reusable block of code to run any selected quiz
def run_quiz(category_id):
    score = 0
    quiz = QUIZ_DATA[category_id]
    
    print(f"\n--- You selected {quiz['topic']} ---")
    
    # LISTS & LOOPS: Convert dictionary keys to a list and loop through them
    question_list = list(quiz["questions"].keys())
    
    for question in question_list:
        correct_answer = quiz["questions"][question]
        
        # USER INPUT: Prompt the user for an answer
        user_answer = input(f"\n{question} ").strip().lower()
        
        # CONDITIONAL STATEMENTS: Verify if the user's answer matches the key
        if user_answer == correct_answer:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer is: {correct_answer}")
            
    print(f"\nYour final score for {quiz['topic']} is: {score}/{len(question_list)}")


# MAIN PROGRAM LOOP
print("Welcome to the Ultimate Quiz Application!")

# LOOPS: Keep the menu running until the user decides to exit
while True:
    print("\nPlease select an option:")
    print("1. Fruits and Vegetables")
    print("2. Animals")
    print("3. Countries")
    print("4. Exit Application")
    
    # USER INPUT: Get category number from user
    user_choice = input("\nEnter your choice (1-4): ").strip()
    
    # CONDITIONAL STATEMENTS & FUNCTIONS: Protect against crash if text is entered
    try:
        option = int(user_choice)
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        continue
        
    # CONDITIONAL STATEMENTS: Route to the correct quiz or exit
    if option in QUIZ_DATA:
        run_quiz(option)
    elif option == 4:
        print("\nThank you for playing! Goodbye! 👋")
        break
    else:
        print("Out of range! Please pick a number from 1 to 4.")
