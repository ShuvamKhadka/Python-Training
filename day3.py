name = "ram"
for i in name:
    print(i)

for index, value in enumerate(name):
    print(index, value)

list1 = [10, 20, 30, 40, 50, 60, 7, 3, 5, 7, 8]

even = []
odd = []
for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
         odd.append(i)
print("Even numbers:", even)
print("Odd numbers:", odd)

age = 20
if age >= 18: #20>18= True
    print("condition 1")
else:
    print("condition 2")

mark = 70
if mark >= 80:
    print("distinction")
elif mark >= 60 and mark < 80:
    print("average")

student = {
"name": "Ram",
"address": "Kathmandu",
"age": 20
}
for key, value in student.items():
    print(key, value)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

print(student.get("roll_no"))

#function
def function_name(a, b):
    print(a * b)

a = 10
b = 20
function_name(a, b)

num1 = input("Enter your number:")
age1 = input(" Enter your age:")
num1 = int(num1)
age1 = int(age1)
print(num1 + age1)

def function_name(c, d):
    sum = c+d
    sub = c-d
    return sum, sub

add, diff = function_name(10, 20)
print(add)
print(diff)
print(add, diff)
result = function_name(10, 20)
print(result)
list1 = [10, 20, 4, 6, 7, 8, 9, 90, 80, 7, 56]
def check_divisible(num):
    for i in list1:
       if i % num == 0:
           print(i)
       else:
            print(i, "is not divisible by", num)

num = int(input("Enter your number: "))
check_divisible(num)

name = "ram"
print(f"My name is {name}")