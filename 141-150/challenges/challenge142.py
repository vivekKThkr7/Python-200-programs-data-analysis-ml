# Create a " Student " class with private " __marks "
# create " get_marks() " to return the marks


class Student:

    def __init__(self, name, marks):
        self.__marks = marks
        self.name = name

    def get_marks(self):
        return self.__marks


student = Student("Ram", 75)

print(student.get_marks())
        
