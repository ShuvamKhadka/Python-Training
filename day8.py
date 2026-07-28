# class Student:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#     def Show_details(self, age):
#         print(f"My name is {self.name} and age is {age}.")

# s1 = Student("Prabin", "Chitwan")
# s1.Show_details(21) 



# class Validator:
#     def __init__(self,email):
#         self.email = email

#     def validate(self, email):
#         if "@" in self.email and self.email.islower():
#             print("valid email")
#         else:
#             print("Invalid email")

# user_email = input("Enter your email: ")
# v1 = Validator(user_email)
# v1.validate(user_email)

# class EmailValidator:
#     def __init__(self, email):
#         self.email = email
#     def is_valid(self):
#         return '@' in self.email and '.' in self.email and self.email.islower()
#         if "@" in self.email and self.email.islower():
#           print("valid email")
#         else:
#           print("Invalid email")

# user_email = input("Enter your email: ")
# v1 = EmailValidator(user_email)
# v1.is_valid()

# def fun1(**kwargs):
#     print(kwargs)

# fun1(name = "ram", address = "Pokhara")

class addition:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def sum1(self):
        sum = 0
        for x in self.args:
            sum += x

        print("The sum is:", sum)
    
    def track1(self):
        for key, value in self.kwargs.items():
            print(f"key is {key} and value is {value}")

v1 = addition(10, 20, 30, value = 40, name = "ram")
v1.sum1()
v1.track1()

        

