# Add a method
#  Method is a function that belongs to an object/class.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")


student1 = Student("Vivek", 27)

student1.introduce()
        