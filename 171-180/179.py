# Refactoring; making Code Cleaner 
#  -> means improving the internal structure of working code without intentionally changing what it does.


def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


def display_receipt(item: str, quantity: int, total: float) -> None:
    print("\n----- RECEIPT -----")
    print("Item:", item)
    print("Quantity:", quantity)
    print(f"Total: {total:.2f}")


def main() -> None:
    item = "Keyboard"
    price = 25.5
    quantity = 3

    total = calculate_total(price, quantity)

    display_receipt(item, quantity, total)


main()




# This is easier to understand than putting every instruction into one long block.
# Two useful details
# The type hint -> None means the function is not intended to return a meaningful value.
# Also, main() is not a special Python keyword. It is an ordinary function name commonly used as the entry point of a program.
# This organization becomes more useful as projects grow.