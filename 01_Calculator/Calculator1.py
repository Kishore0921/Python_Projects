print("--- Basic Calculator Program ---")

# Take numeric inputs
num1 = float(input("Enter number 1 Value: "))
num2 = float(input("Enter number 2 Value: "))

# Take the operation as a string (do not use eval here)
operation = input("Enter operation to perform (+, -, *, /, %, **): ")

# Perform calculation based on the operator
if operation == "+":
    print("Addition of two numbers is:", num1 + num2)
elif operation == "-":
    print("Subtraction of two numbers is:", num1 - num2)
elif operation == "*":
    print("Multiplication of two numbers is:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Division of two numbers is:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "%":
    print("Modulus of two numbers is:", num1 % num2)
elif operation == "**":
    print("Exponentiation of two numbers is:", num1 ** num2)
else:
    print("Invalid operation entered.")
