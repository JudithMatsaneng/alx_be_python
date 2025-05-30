# multiplication_table.py

def print_multiplication_table():
    # Get user input for number
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print the multiplication table
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    print_multiplication_table()
# multiplication_table.py
