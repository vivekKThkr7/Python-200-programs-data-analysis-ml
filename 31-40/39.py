age = int(input("Enter your age: "))
education = input('Enter your education: ')
experience = int(input("Enter yoars of experience: "))
internship = input("Have you done Intership? ")

if age >=18 and age <=35:
    if education == "graduation":
        if experience >= 1 or internship == "yes":
            print("your are eligible")
        else: 
            print("You need to have either 1 years of experience or must be done internship.")

    else:
        print("Graduation is required")

else:
    print("Age requirement not satisfied.")
    