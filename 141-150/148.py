# super() with overriding

class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):

    def introduce(self):
        super().introduce()
        print("I am also a student")

student = Student()

student.introduce()

