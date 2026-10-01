# Method Overriding
# A class provides its own version of a method inherited form the parent

class Person:
    def intruduce(self):
        print("I am a person")

class Student(Person):
    def intruduce(self):
        print("I am a student")


person = Person()
student = Student()

person.intruduce()
student.intruduce()


# The method has the same name  " introduce() " but different behaviour

