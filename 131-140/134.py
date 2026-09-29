# The _init_() method

#  This is a special method that runs automatically when an object is created. 



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Vivek", 26)

print(student1.name)
print(student1.age)

        