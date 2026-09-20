# ask for 5 numbers and find largest and Smallest.

numbers = []

for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
