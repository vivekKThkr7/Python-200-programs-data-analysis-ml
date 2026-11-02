# Ask the user for 5 numbers and print the number of items using len()

numbers = []

for i in range(5):
    number = int(input("Enter number: "))
    numbers.append(number)

print(len(numbers))