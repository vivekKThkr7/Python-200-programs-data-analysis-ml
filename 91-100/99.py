# Multiple Function together

def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

def calculate_average(numbers):
    total = calculate_total(numbers)
    return total / len(numbers)


marks = [75, 82, 45, 91, 60]

total = calculate_total(marks)
average = calculate_average(marks)

print("Total:", total)
print("Average:", average)