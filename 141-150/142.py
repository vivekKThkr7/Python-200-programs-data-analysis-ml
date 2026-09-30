# Getter method: is a method used to get/read a value.

class Student:

    def __init__(self, name, marks):
        self.__marks = marks
        self.name = name

    def get_marks(self):
        return self.__marks


student = Student("Ram", 75)

print(student.get_marks())
        