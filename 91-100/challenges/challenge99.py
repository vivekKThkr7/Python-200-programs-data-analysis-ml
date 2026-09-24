
# create three functions 
# calculate_total()
# calculate_average()
# count_passed()


def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def calculate_average(numbers):
    total = calculate_total(numbers)
    return total / len(numbers)


def count_passed(numbers):
    count = 0

    for number in numbers:
        if number >= 40:
            count += 1

    return count


marks = [75, 82, 45, 91, 60]

total = calculate_total(marks)
average = calculate_average(marks)
passed = count_passed(marks)

print("Total:", total)
print("Average:", average)
print("Passed:", passed)