# Dubbing: finding mistakes systematically.
#  Dubugging is the process of finding, understanding, and fixing mistakes in a program.


# Calcluate a discount

def calculate_discount(price: float, discount_percent: float) -> float:
    print("DEBUG: Price =", price)
    print("DEBUG: Discount percentage =", discount_percent)

    discount = price * (discount_percent / 100)

    print("DEBUG: Discount amount =", discount)

    final_price = price - discount

    print("DEBUG: Final price =", final_price)

    return final_price


result = calculate_discount(100, 15)

print("Amount to pay:", result)


# A useful debugging method
# 1. Identify the incorrect output.
# 2. Check the values entering the function.
# 3. Check the calculation that produces the wrong result.
# 4. Check the returned value.
# 5. Fix the actual cause and test again.