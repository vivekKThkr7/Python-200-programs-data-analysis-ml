# Child gets parents + Child methods

class person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

class Student(person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_marks(self):
        print("Marks:", self.marks)


student = Student("Sita", 80)

student.introduce()
student.show_marks()



# from Person:
# introduce()

# from Student:
# show_marks()