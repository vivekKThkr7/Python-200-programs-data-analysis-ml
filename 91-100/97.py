# Function for Average

def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


marks = [70, 80, 90, 60]

average = calculate_average(marks)

print("Average:", average)
