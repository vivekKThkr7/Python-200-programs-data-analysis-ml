# Challenge 145
# Person -> Student
# Student should have name and marks.
# Use super().__init__().

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks


student = Student("Sita", 82)
print("Name:", student.name)
print("Marks:", student.marks)
