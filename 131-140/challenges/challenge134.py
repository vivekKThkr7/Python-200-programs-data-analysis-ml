# reate two Students objects: Ram, Sita, with different ages 
# print thier information

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ram", 20)
student2 = Student("Sita", 22)

print("Name:", student1.name)
print("Age:", student1.age)

print("Name:", student2.name)
print("Age:", student2.age)