# Creating Custom Exceptions
# Custom exption is an exception class that we define to represent an applicatiob-specific error.


class InsufficientStockError(Exception):
    pass
# Exception is the parent class.
# pass means there is no additional code inside this class for now.


def sell_stock(stock: int, quantity: int) -> int:
    if quantity > stock:
        raise InsufficientStockError("Not enough stock available.")

    return stock - quantity


stock = 5

try:
    remaining_stock = sell_stock(stock, 8)
    print("Remaining stock:", remaining_stock)

except InsufficientStockError as error:
    print("Sale failed:", error)


