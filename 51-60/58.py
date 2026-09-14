number = int(input("Enter a number: "))
for divisor in range(1, number+1):
    if number % divisor == 0:
        print(divisor)