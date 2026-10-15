# Inventory Management System
# Create the product class
# Use a Product dataclass with these fields: name, price, quantity
# Add a method: stock_value()
# Store multiple products, Create the required functions
# Validate stock sales, Display the inventory




from dataclasses import dataclass


class InsufficientStockError(Exception):
    """Raised when a sale requests more items than are in stock."""


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def stock_value(self) -> float:
        return self.price * self.quantity


def add_product(inventory: list[Product], name: str, price: float, quantity: int) -> Product:
    product = Product(name, price, quantity)
    inventory.append(product)
    return product


def show_inventory(inventory: list[Product]) -> None:
    for product in inventory:
        print(f"{product.name} - Qty: {product.quantity} - Value: {product.stock_value():.2f}")


def sell_product(product: Product, quantity: int) -> None:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    if quantity > product.quantity:
        raise InsufficientStockError("Not enough stock.")
    product.quantity -= quantity


def show_total_value(inventory: list[Product]) -> float:
    total = sum(product.stock_value() for product in inventory)
    print(f"Total inventory value: {total:.2f}")
    return total


def attempt_sale(product: Product, quantity: int) -> None:
    print(f"Selling {quantity} {product.name}...")
    try:
        sell_product(product, quantity)
        print("Sale completed.")
    except InsufficientStockError as error:
        print(f"Sale failed: {error}")
    except ValueError as error:
        print(f"Sale failed: {error}")
    print()


def main() -> None:
    inventory: list[Product] = []
    add_product(inventory, "Keyboard", 25, 10)
    add_product(inventory, "Mouse", 15, 20)

    print("----- INVENTORY -----\n")
    show_inventory(inventory)
    print()

    attempt_sale(inventory[0], 3)    # successful
    attempt_sale(inventory[1], 50)   # insufficient stock
    attempt_sale(inventory[1], 0)    # invalid quantity

    print("----- UPDATED INVENTORY -----\n")
    show_inventory(inventory)
    print()
    show_total_value(inventory)


if __name__ == "__main__":
    main()