# Challenge 149 ⭐
# Dog and Cat both have speak().
# Use both objects in one list and one loop.

class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
