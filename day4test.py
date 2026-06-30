def add_number(first_num, second_num):
    """
    Add two number and return the result
    """
    return first_num + second_num

def calc(first_num, second_num, op):
    """
    calculate two number based on the operator and return the result
    """
    if op == "+":
        return first_num + second_num
    elif op == "-":
        return first_num - second_num
    elif op == "*":
        return first_num * second_num
    elif op == "/":
        return first_num / second_num
    elif op == "%":
        return first_num % second_num
    else:
        return "Invalid operator"

def calculator(a, b):
    print(a+b)

result = calculator
sum1 = result(10, 30)
print(sum1)

    