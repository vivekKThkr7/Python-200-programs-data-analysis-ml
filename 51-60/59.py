# Find the Largest Number From User Input

largest = None
for i in range(5):
    number = float(input("Enter a number: "))

    if largest is None or number > largest:
        largest = number
print("Largest: ", largest)