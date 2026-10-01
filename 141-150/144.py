# Inheritance allows one class to reuse properties and method from another class.
# Suppose "person" is a general type and "Student" & "teacher" are most specific types of people.

class Person:

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print("My name is", self.name)


class Student(Person):
    pass


student = Student("Vivek")

student.introduction()


# What happen here?

# Student inherited form Person
# Therefore the Student object can use
# student.introduction()