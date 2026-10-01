# Child class with its own attribute
# A child has its own data in addition to inheerited data.

class person:
    def __init__(self, name):
        self.name = name

class Student(person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

student = Student("Ram", 65)


print(student.name)
print(student.marks)



# New Concept " super() "
# Means: Run the parent class's __init__()
