# Challenge 143
# Add set_marks() and only allow marks from 0 to 100.

class Student:
    def __init__(self, marks):
        self.__marks = 0
        self.set_marks(marks)

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks. Marks must be between 0 and 100.")


student = Student(75)
print("Marks:", student.get_marks())

student.set_marks(90)
print("Marks:", student.get_marks())

student.set_marks(120)
print("Marks:", student.get_marks())
