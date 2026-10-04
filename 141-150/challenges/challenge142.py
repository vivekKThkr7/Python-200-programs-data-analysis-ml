# Challenge 142
# Create a Student class with private __marks.
# Create get_marks() to return the marks.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student = Student(85)
print("Marks:", student.get_marks())
