def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            print("Error: Cannot divide by zero.")

        result = num / denom
        print(f"The result of the division is {result}")
    except ValueError:
        print("Error: Please enter numeric values only.")
