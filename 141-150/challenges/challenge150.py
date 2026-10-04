# Build a small Employee management System
# Create: Employee, Developer, Designer, Manager
# Employee should contain:
# name, work()
# For examople:
# Developer -> Wrtiting code
# designer -> Designing UI
# Manager -> Managing team
# Create at least 4 employee objects in one list.
# then:
# for employee in employees:
#   employee.work()
# Your output should resemble:
# Ram -> Writing code 
# Sita -> Designing UI
# Hari -> Managing team
# Gita -> Writing code
# Don't make it complicated.
# The goal is to prove that you understand. 




# Challenge 150 ⭐⭐⭐
# Small Employee Management System.
# Create Employee, Developer, Designer, and Manager.

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "→ Working")


class Developer(Employee):
    def work(self):
        print(self.name, "→ Writing code")


class Designer(Employee):
    def work(self):
        print(self.name, "→ Designing UI")


class Manager(Employee):
    def work(self):
        print(self.name, "→ Managing team")


employees = [
    Developer("Ram"),
    Designer("Sita"),
    Manager("Hari"),
    Developer("Gita")
]

for employee in employees:
    employee.work()
