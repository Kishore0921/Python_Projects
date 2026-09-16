print("Basic calculator program using functions")

#In functions all operations are performed using functions. Each operation is defined in a separate function, and the results are printed after calling each function.
#Global variables can be accessed inside functions, but it's better to pass them as parameters for clarity and maintainability.
a = eval(input("Enter number 1 Value: ")) #Global variable
b = eval(input("Enter number 2 Value: ")) #Global variable

def add(a, b):
    return a + b
result = add(a, b) #Calling the add function and storing the result in a variable [Main part calling function]
print("Addition of two numbers is:", result)

def subtract(a, b):
    return a - b
result = subtract(a, b) #Calling the subtract function and storing the result in a variable [Main part calling function]
print("Subtraction of two numbers is:", result)

def multiply(a, b):
    return a * b
result = multiply(a, b) #Calling the multiply function and storing the result in a variable [Main part calling function]
print("Multiplication of two numbers is:", result)

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
result = divide(a, b) #Calling the divide function and storing the result in a variable [Main part calling function]        
print("Division of two numbers is:", result)

def modulus(a, b):
    return a % b
result = modulus(a, b) #Calling the modulus function and storing the result in a variable [Main part calling function]
print("Modulus of two numbers is:", result)

def exponentiate(a, b):
    return a ** b
result = exponentiate(a, b) #Calling the exponentiate function and storing the result in a variable [Main part calling function]
print("Exponentiation of two numbers is:", result)