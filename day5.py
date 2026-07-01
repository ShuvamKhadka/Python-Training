from day5test import calculator
#args and kwargs

# def mul_no(*args, **kargs):
#     print(args)
#     print(kargs)
   
# mul_no(2, 4, 6, value = 50)

# def add_no(*args, **kargs):
#     sum = 0
#     for i in args:
#         sum += i
#     print("The sum of the numbers is:", sum)

# add_no(10, 20, 30, 40)
    
# def mul_no(*args, **kargs):
#     print(args)
#     print(kargs)
   
# mul_no(20, 40, 60, 50, value = 50, name = "Prabin")

# def mul_no(a, *args, **kargs):
#     print(args)
#     print(kargs)
   
# mul_no(20, 40, 60, 50, value = 50, name = "Prabin")

# def mul_no(a, b,*args, **kargs):
#     print(args)
#     print(kargs)
   
# mul_no(20, 40, 60, 50, value = 50, name = "Prabin")

#numnber1, number2, operator 
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %): ")
result = calculator(number1, number2, operator=operator)
print(result)
    
