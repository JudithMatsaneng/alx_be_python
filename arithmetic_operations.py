def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
# Example usage:
if __name__ == "__main__":
    print(perform_operation(6, 5, 'add'))        # Output: 11
    print(perform_operation(6, 5, 'subtract'))   # Output: 1
    print(perform_operation(6, 5, 'multiply'))   # Output: 30
    print(perform_operation(6, 5, 'divide'))     # Output: 1.2
    print(perform_operation(6, 0, 'divide'))     # Output: Error: Division by zero
    print(perform_operation(6, 5, 'modulus'))     # Output: Error: Invalid operation
