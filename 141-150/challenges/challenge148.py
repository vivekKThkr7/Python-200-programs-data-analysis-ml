# Challenge 148
# Override a parent method and also call the parent's version using super().

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)


class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am a student.")


student = Student("Hari")
student.introduce()
