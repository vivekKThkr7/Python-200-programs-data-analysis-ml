# Filter Even Numbers

numbers = [10, 15, 20, 25, 30, 35, 40, 50]

even_number = []

for number in numbers:
    if number % 2 == 0:
        even_number.append(number)   # append() : means to add something in that list.

print("Even numbers: ", even_number)

