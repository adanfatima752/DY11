def divide_two_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
