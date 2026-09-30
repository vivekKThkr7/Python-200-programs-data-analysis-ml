# Create
# class Student:
# with name, marks and a  method:
# check_result()
# return: "pass"
# when marks >= 40, otherwise: "Fail"


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):

        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Ram", 75)

print(
    student1.name,
    "-",
    student1.marks,
    "-",
    student1.check_result()
)
