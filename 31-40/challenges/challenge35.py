marks = float(input("Enter obtained marks: "))
attendance_rate = float(input("Enter attendance rate: "))

if marks < 40 and attendance_rate < 75:
    print("Failed due to low marks and low attendance")

elif marks < 40:
    print("Failed due to low marks")

elif attendance_rate < 75:
    print("Failed due to low attendance")

else:
    print("Pass")