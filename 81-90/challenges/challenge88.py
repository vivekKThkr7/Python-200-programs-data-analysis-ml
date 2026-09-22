# Find largest and second largest from the list.

numbers = [10, 20, 40, 50, 60, 80, 20, 45, 67, 88]

largest = numbers[0]
second_largest = numbers[0]

for number in numbers: 
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Largest:", largest)
print("Second largest:", second_largest)