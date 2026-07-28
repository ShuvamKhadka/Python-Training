# class Employee:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

# class Developer(Employee):
#     def __init__(self, name, address, language):
#         self.language = language
#         super().__init__(name, address)

# d1 = Developer("Ram", "Pokhara", "python")
# print(d1.name) 

# class Employee:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#     def display_detail(self):
#         print(self.name)
#         print(self.address)

# class Developer(Employee):
#     def __init__(self, name, address, language):
#         self.language = language
#         super().__init__(name, address)
#     def show_detail(self):
#         super().display_detail()
#         print(self.language)
            
# d1 = Developer("Ram", "pokhara", "python")
# d1.show_detail() 

class Calculator:   
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    
    def modulo(self, num1, num2):
        return num1 % num2
    
my_calc = Calculator()

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Enter the operator:")

if op == "+":
   print(f"{num1} + {num2} = {my_calc.add(num1, num2)}")

elif op == "-":
   print(f"{num1} - {num2} = {my_calc.subtract(num1, num2)}")

elif op == "*":
   print(f"{num1} * {num2} = {my_calc.multiply(num1, num2)}")

elif op == "/": 
   print(f"{num1} / {num2} = {my_calc.divide(num1, num2)}")

elif op == "%":
    print(f"{num1} % {num2} = {my_calc.modulo(num1, num2)}")

else:
    print("Invalid operator")