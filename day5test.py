def calculator(*args, **kargs):
    operator = kargs.get("operator")
    number1, number2 = args
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "%":
        return number1 % number2
    else:
        return "Invalid operator"