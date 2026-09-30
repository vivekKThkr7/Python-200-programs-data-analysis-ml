# Add a method:
# introduce()
# that prints the student's name and age

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")


student1 = Student("Ram", 20)

student1.introduce()