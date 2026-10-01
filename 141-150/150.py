# Mini OOP System
class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working")


class Developer(Employee):

    def work(self):
        print(self.name, "is writing code")


class Designer(Employee):

    def work(self):
        print(self.name, "is designing")


employees = [
    Developer("Ram"),
    Designer("Sita"),
    Developer("Hari")
]

for employee in employees:
    employee.work()


# Output:

# Ram is writing code
# Sita is designing
# Hari is writing code
# What concepts are here?
# Employee
#    ↓
# Developer
# Designer

# Inheritance:

# Developer → Employee
# Designer  → Employee

# Overriding:

# Developer.work()
# Designer.work()

# Polymorphism:

# employee.work()

# The same line produces different behavior.

# And:

# employees = [...]

# is a list of different objects.

# This brings together several things you've already learned:

# List
# +
# Loop
# +
# Class
# +
# Object
# +
# Inheritance
# +
# Method overriding
# +
# Polymorphism

# 🔥 This is real OOP thinking.