# Given:  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a new list containing only even numbers using list comprehension.

# Expected: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
