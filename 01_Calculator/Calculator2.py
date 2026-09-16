print("Calculator Program using match-case statement")

num1 = eval(input("Enter number 1 Value: "))
num2 = eval(input("Enter number 2 Value: "))
operation = input("Enter operation to perform (+, -, *, /, %, **): ")

match operation:
    case "+":
        print("Addition of two numbers is:", num1 + num2)
    case "-":
        print("Subtraction of two numbers is:", num1 - num2)
    case "*":
        print("Multiplication of two numbers is:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Division of two numbers is:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    case "%":
        print("Modulus of two numbers is:", num1 % num2)
    case "**":
        print("Exponentiation of two numbers is:", num1 ** num2)
    case _:
        print("Invalid operation entered.")