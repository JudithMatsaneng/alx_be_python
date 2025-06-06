def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

if __name__ == "__main__":
    main()
# This code imports the perform_operation function from the arithmetic_operations module
# and uses it to perform arithmetic operations based on user input.
# The main function prompts the user for two numbers and an operation,
# then calls perform_operation and prints the result.

# >>> python .\main.py
#Arithmetic Operations
#Enter the first number: 5
#Enter the second number: 6
#Enter the operation (add, subtract, multiply, divide): add
#Result: 11.0
