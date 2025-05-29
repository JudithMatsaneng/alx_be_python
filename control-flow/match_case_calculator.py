# match_case_calculator.py

def calculator():
    # Get user input for numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get user input for operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform calculation using Match Case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Cannot divide by zero.")
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")

if __name__ == "__main__":
    calculator()
# This code implements a simple calculator that performs addition, subtraction, multiplication, or division based on user input.
# It uses a match-case structure to handle different operations.
# This code implements a simple calculator that performs addition, subtraction, multiplication, or division based on user input.
# It uses a match-case structure to handle different operations.
