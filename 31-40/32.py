# Check whether someone qualifies for a job.
#  Age at least 18
# Education must be "bachelor" 
#  Experience at least 1 years

age = int(input("Enter your age: "))
education = input("Enter your education level: ")
experience = float(input("Enter years of experience: "))

if age >=18 and education=="bachelor" and experience >=1:
    print("You are eligible")

else:
    print("You are not eligible")
    