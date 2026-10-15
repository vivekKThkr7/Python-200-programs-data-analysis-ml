# imagine an inventory system where customers cannot purchase more items that the store has available.
# create InsufficientStockError(Exception):
#   pass

# Then write:
# sell_stock(stock, quantity)



# Rules
# - If quantity is zero or negative, raise ValueError.
# - If quantity exceeds stock, raise InsufficientStockError.
# - Otherwise, return the remaining stock.



class InsufficientStockError(Exception):
    pass


def sell_stock(stock: int, quantity: int) -> int:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    if quantity > stock:
        raise InsufficientStockError("Not enough stock available.")
    return stock - quantity


stock = 10
for requested in [3, 15, 0, -2]:
    try:
        remaining = sell_stock(stock, requested)
        print(f"Sale successful. Remaining stock: {remaining}")
    except InsufficientStockError as error:
        print(f"Sale failed: {error}")
    except ValueError as error:
        print(f"Sale failed: {error}")