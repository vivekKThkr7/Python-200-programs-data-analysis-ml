units = int(input("Enter electricity units: "))

if units >=0 and units <=100:
    bill = units*2
elif units <=200:
    bill = units*3
elif units <=300:
    bill = units *5

else:
    bill = units*7

print("Electricity Bill : ", bill)