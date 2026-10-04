# Challenge 147
# Create Person.introduce() and Student.introduce().
# Student overrides the parent's version.

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, I am a person named", self.name)


class Student(Person):
    def introduce(self):
        print("Hello, I am a student named", self.name)


person = Person("Ram")
student = Student("Sita")

person.introduce()
student.introduce()
