age = int(input("Enter your age: "))
income = float(input("Enter your montly income: "))
student = input("Are you a student?")

if student == 'yes':
    if income < 2000:
        print("Focus on education and building skills.")
    else:
        print("Balance education, savings, and building skills")
else:
    if income< 3000:
        print("Focus on increasing income and building skills")
    elif income <=7000:
        print("Focus on saving and career growth")
    else:
        print("Focus on savings, investment, and long-term planning")