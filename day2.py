list1 = [10, 20, 30, 40, 50, "ram"]
#access, modify, delete, insert
list1[0] = "hari"
print(list1)
list1.remove("ram")#to remove from index

print(list1)

list1.append(90)#insert value at the end
print(list1)

t1 = (1, 2, 3)
print(type(t1))

#dictionary
student = {
    "name": "Ram",
    "address": "Kathmandu",
    "mobile": "98054",
    "name": "hari"
}
student["name"] = "Shyam"
print(student["name"])

name = student.get("name1", "custom default value")
print(name)

name = student.pop("name")
student["name"] = "shyam"
student["address"] = "kathmandu"
print(student)

#set
s1 = {10, 10, "ram", 30, 10, 10}
s1.add(90)
l1 = [10, 10, 10]
print(s1)
print(l1)