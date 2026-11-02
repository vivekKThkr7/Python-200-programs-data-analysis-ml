# Why type conversion matters?

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1+num2)   # it concatinate the value only

# so to get the output correct

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1+num2)  # this produe the sum of num1 and num2

