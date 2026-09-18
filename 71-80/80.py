# Simple Student marks Analyzer.

# marks = [75, 82, 45, 91, 60]

# We want:

# total
# average
# highest
# lowest
# number of passed students


marks = [75, 82, 45, 91, 60]

total = 0
passed = 0

for mark in marks:
    total +=mark

    if mark >= 40:
        passed +=1

average = total / len(marks)

print("Total: ", total)
print("Average: ", average)
print("Highest: ", max(marks))
print("Lowest:", min(marks))
print("Passed:", passed)