# Check  number prime or not

number = int(input("Enter a number: "))
if number < 2:
    print("Not Prime")
else:
    is_Prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_Prime = False
            break

    if is_Prime:
        print("Prime")

    else:
        print("Not Prime")
        