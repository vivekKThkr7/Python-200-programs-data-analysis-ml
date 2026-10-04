# Challenge 146
# Add check_result() to Student.
# Return Pass or Fail.

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


student = Student("Hari", 75)
print(student.name, "-", student.marks, "-", student.check_result())
