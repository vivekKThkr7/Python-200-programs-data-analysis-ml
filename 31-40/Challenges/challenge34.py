number = int(input("Enter an integer: "))
if number<0:
    if number % 2 == 0:
        print("Negative even")
    else:
        print("negative odd")

elif number>0:
    if number%2==0:
        print("Positive Even")
    else:
        print("Positive odd")

else:
    print("Zero")