# class College:
#     college_name = "EEC"

#     def __init__(self, location):
#         self.location = location

#     def show_details(self):
#         pass

# c1 = College("Sanepa Height")
# print(c1.location)
# print(College.college_name)
# c1.show_details()

#setattr, getattr, hasattr
#setattr(object, attribute_name, new_value)
#getattr(object, attribute_name, default_name if need)
#hasattr(object, attribute_name)give True or False if attribute exist give true else false

# class Person:
#     def __init__(self, name):
#         self.name = name

# p = Person("Alice")

# print(hasattr(p, "name"))
# print(hasattr(p, "name"))

# print(getattr(p, "name"))

# setattr(p, "name", "Bob")
# setattr(p, "age", 21)

# print(p.name)
# print(p.age)

from email.headerregistry import Address


class Dict1:
    def __init__(self):

        self_info = {
            "name" : "Aayush",
            "age" : 25,
            "address" : "KTM"
        }

d1 = Dict1()  
print(hasattr(d1, "name"))
print(hasattr(d1, "age"))
print(hasattr(d1, "address"))

print(getattr(d1, "name"))
print(getattr(d1, "age"))
print(getattr(d1, "address"))

setattr(d1, "name", "Aayush")
setattr(d1, "age", 25)
setattr(d1, "address", "KTM")

