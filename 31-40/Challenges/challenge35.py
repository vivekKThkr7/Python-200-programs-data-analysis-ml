marks = float(input("Enter obtained marks: "))
attendance_rate = float(input("Enter the rate of attendance out of 100: "))
if marks >= 40 and attendance_rate >=75:
    print("Pass")
elif marks <=40 and attendance_rate >=75:
    print("Faied due to low score")
elif marks >= 40 and attendance_rate <=75:
    print("Failed due to low attendance rate.")

else:
    print("invalid Inputs")