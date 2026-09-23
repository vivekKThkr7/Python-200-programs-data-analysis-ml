# Create a function and find smallest number.

def smallest_number(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


numbers = [10, 20, 60, 70, 80, 40, 30]

result = smallest_number(numbers)

print(result, "is the smallest number")
