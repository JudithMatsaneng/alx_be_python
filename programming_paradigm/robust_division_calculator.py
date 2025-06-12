def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = numerator / denominator
        if result % 1 == 0:
            return f"The result of the division is {int(result)}.0"
        else:
            return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

