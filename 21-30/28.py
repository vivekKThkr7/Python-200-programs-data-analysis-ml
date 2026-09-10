age = int(input("Enter your age: "))
is_student = input("Are you a students? ")

if age >= 60 or is_student == "yes":
    print("Discount available")

else:
    print("No discount")
