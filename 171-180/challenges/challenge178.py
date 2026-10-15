# BUG: the original code did `discount = price * discount_percent`.
# With discount_percent = 15 that gives 100 * 15 = 1500, i.e. 1500 times
# too big, because 15 means 15 percent (15 / 100 = 0.15), not 15 times.
# FIX: divide the percentage by 100 to convert it to a proportion.
 
def calculate_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    # print("DEBUG discount:", discount)  # temporary debugging
    final_price = price - discount
    return final_price
 
 
price = 100
discount_percent = 15
result = calculate_discount(price, discount_percent)
print("Final price:", result)  # 85.0
 
# Second test
print("Final price:", calculate_discount(250, 20))  # 200.0
 
