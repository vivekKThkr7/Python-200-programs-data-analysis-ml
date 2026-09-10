marks = float(input("Enter marks: "))

if marks >= 80:
    print("Grade : A")

elif marks >=60 and marks <=79:
    print("Grade : B")

elif marks >=40 and marks<=59:
    print("Grade : C")

elif marks<=40:
    print("Grade : Fail")

else:
    print("!!!!")


