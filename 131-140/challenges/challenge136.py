# Create: class Calculator:
#  with methods:
# add(), subtract (), multiply()
# Each should return the result


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print("Add:", calculator.add(10, 5))
print("Subtract:", calculator.subtract(10, 5))
print("Multiply:", calculator.multiply(10, 5))
