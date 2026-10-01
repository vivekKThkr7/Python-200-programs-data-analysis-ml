# Setter method : used to change/update a value in a controlled way

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks

        else:
            print("Invalid Marks")

student = Student("Ram", 50)
print(student.get_marks())
student.set_marks(90)
print(student.get_marks())

