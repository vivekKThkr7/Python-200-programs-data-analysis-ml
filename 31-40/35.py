age = int(input("Enter your age:"))
if age > 0 and age < 5:
    price = 0

elif age <=12:
    price = 10

elif age <=59:
    price = 20

else:
    price = 12

print("Ticket price: ", price)