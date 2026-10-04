# Challenge 144
# Create Person with name and introduce().
# Create Student(Person) and show Student can use introduce().

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)


class Student(Person):
    pass


student = Student("Ram")
student.introduce()
