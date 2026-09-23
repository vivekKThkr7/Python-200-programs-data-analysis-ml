# Function for largest number

def find_largestNumber(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

numbers = [10, 20, 60, 70, 80, 40, 30]

result = find_largestNumber(numbers)
print("largest: ", result)