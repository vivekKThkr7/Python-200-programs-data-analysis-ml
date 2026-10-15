# Program 180. mini inventory Magagement System.


from dataclasses import dataclass

class InsufficientStockError(Exception):
    pass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def stock_value(self) -> float:
        return self.price * self.quantity


def sell_product(product: Product, quantity: int) -> None:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    if quantity > product.quantity:
        raise InsufficientStockError(
            f"Not enough {product.name} in stock."
        )

    product.quantity -= quantity


def show_inventory(products: list[Product]) -> None:
    print("\n_______INVENTORY______")

    for product in products:
        print(
            f"{product.name} | "
            f"Quantity: {product.quantity} | "
            f"Stock value: {product.stock_value():.2f}"
        )


def main() -> None:
    products = [
        Product("Keyboard", 25.0, 10),
        Product("Mouse", 15.0, 20),
    ]

    show_inventory(products)

    try:
        sell_product(products[0], 3)
        print("\nSale completed successfully.")

    except (ValueError, InsufficientStockError) as error:
        print("\nSale failed:", error)

    show_inventory(products)

    total_value = sum(
        product.stock_value()
        for product in products
    )

    print(f"\nTotal inventory value: {total_value:.2f}")


main()