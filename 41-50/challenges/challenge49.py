# Use nested loops to print a right-angled triangle of five rows of stars.

for row in range(1, 6):
    for _ in range(row):
        print("*", end="")
    print()
