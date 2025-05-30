# pattern_drawing.py

def draw_pattern():
    # Get user input for pattern size
    size = int(input("Enter the size of the pattern: "))

    # Initialize row counter
    row = 0

    # Draw the pattern using while loop and nested for loop
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1

if __name__ == "__main__":
    draw_pattern()
# pattern_drawing.py
