print("Welcome to the Quiz Application! Please select an option:")

option = input("1.Fruits and Vegetables \n2.Animals \n3.Countries \n Enter your choice (1, 2, or 3): ")

if option == "1":
    print("You selected Fruits and Vegetables.")
    def Fruits_and_Vegetables():
        score = 0
        questions = {
            "What fruit is known as the 'king of fruits'?": "durian",
            "Which vegetable is known for its high vitamin A content?": "carrot",
            "What fruit is typically red and has seeds on the outside?": "strawberry"
        }
        for question, answer in questions.items():
            user_answer = input(question + " ").lower()
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {answer}.")
        print(f"Your final score is: {score}/{len(questions)}")
    Fruits_and_Vegetables()
