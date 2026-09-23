# Create a " function calculate_sum(numbers) "   
## Don't use sum()

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [24, 25]

result = calculate_sum(numbers)

print(result)