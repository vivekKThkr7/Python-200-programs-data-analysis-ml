age = int(input("Enter your age: "))
education = input("Enter level of education: ")
experience = int(input("Enter year of experience: "))

if age >= 18 and age <=25:
    if education == "bachelor":
        if experience >= 1:
            print("Elligible for Job")
        else:
            print("Low experience")
    else:
        print("Low education")
else:
    print("Out of age range")
    