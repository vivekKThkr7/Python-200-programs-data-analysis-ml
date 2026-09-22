# from the given list, create a new list containg only even numbers

numbers = [5, 10, 15, 20, 25, 30, 40, 50, 65]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)