# Ask for 5 numbers, store them in list, then calculate: Total & Average.
numbers = []

for i in range(5):
    number = int(input("Enter numbers: "))
    numbers.append(number)

total = 0

for number in numbers:
    total +=number

average = total/len(numbers)

print(numbers)
print(total)
print(average)