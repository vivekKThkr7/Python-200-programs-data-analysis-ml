# Create
# class Student 
# Use _int_() to store: name, age
# Create one student object

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ram", 20)

print("Name:", student1.name)
print("Age:", student1.age)
