# built a simple voting eligibility checker.

age = int(input("Enter your age: "))

if age >= 18:
    citizenship = input("Are you a citizen? ")

    if citizenship == "yes":
        print("You are eligible to vote")
    else:
        print("You must be a citizen to vote")
else:
    print("You are too young to vote")