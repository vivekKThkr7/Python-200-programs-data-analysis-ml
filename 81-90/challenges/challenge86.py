# Create a list containg only the puplicate values  (Do not repeat values)

numbers = [10, 20, 20, 25, 25, 30, 35, 40, 45, 45, 50, 50, 60, 70, 90, 99]

duplicate_number = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicate_number:
        duplicate_number.append(number)


print(duplicate_number)