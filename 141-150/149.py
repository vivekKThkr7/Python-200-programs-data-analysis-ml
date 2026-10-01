# Polymorphism
# Different object can respond to the same method name in different ways.

class Dog:
    def speak(self):
        print("woof")

class Cat:
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
