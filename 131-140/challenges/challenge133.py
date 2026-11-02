# Create
# class Student 
# Use __init__() to store the name and age.
# Create one student object

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ram", 20)

print("Name:", student1.name)
print("Age:", student1.age)
