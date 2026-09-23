
# create three functions 
# calculate_total()
# calculate_average()
# count_passed()


def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += numbers

    return total

def calculate_average(numbers):
    total = calculate_average(numbers)
    return total / len(numbers)

def count_passed(numbers):
    count = 0
    if numbers < 50:
        return count+=1
    else:
        return count-=1


marks = marks = [75, 82, 45, 91, 60]

total = calculate_total(marks)
average = calculate_average(marks)
count_passed = count_passed(marks)

print(calculate_total)
print(calculate_average)
print(count_passed)