# Grade calculator: 80+ = A, 60-79.99 = B, 40-59.99 = C, below 40 = Fail.

marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Please enter marks between 0 and 100.")
elif marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
