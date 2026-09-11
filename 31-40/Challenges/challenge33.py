a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print(a, " is smallest number")
elif b < c and b < c:
    print(b, " is smallest number")
else:
    print(c, " is smallest number")
    