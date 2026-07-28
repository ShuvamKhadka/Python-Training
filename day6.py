# status = [
#     {
#         "name" : "Prabin",
#         "active" : True
#     },
#     {
#         "name" : "Rocky",
#         "active" : False
#     },
#     {
#         "name" : "Aayush",
#         "active" : True
#     },
#     {
#         "name" : "Nischal",
#         "active" : False
#     }
# ]

# def get_active_users(user):
#     active_user = []
#     for x in user:
#         if x["active"] == True:
#             active_user.append(x)
#     print(active_user)

# get_active_users(status)


#list Comprehension

# marks = [10, 20, 30, 40, 50]

# for index, i in enumerate[int](marks):
#     if index == 2:
#         continue
#     print(i)

age = [10, 20, 3, 4, 5, 70]
#l1 = [return value for i in iterator condition]

# even = [i for i in age if i%2 == 0]
# print(even)
# even = []

# for i in age:
#     if i%2 == 0:
#         even.append(i)
# print(even)

odd = [i for i in age if i%2 != 0]
print(odd)