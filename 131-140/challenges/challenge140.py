# Build a Student Class Analyzer.

# Create:

# class Student:

# Each student should have:

# name
# marks

# And methods:

# display()
# check_result()

# Create at least 3 student objects.

# Example:

# Ram - 75 - Pass
# Sita - 35 - Fail
# Hari - 82 - Pass



class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(
            self.name,
            "-",
            self.marks,
            "-",
            self.check_result()
        )

    def check_result(self):

        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Ram", 75)
student2 = Student("Sita", 35)
student3 = Student("Hari", 82)

student1.display()
student2.display()
student3.display()
