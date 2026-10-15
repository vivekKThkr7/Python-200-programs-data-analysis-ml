# product dataclass
# Create a aProduct dataclass containing: name, price, quantity
# Create at least three product objects.
# Requirements:
# 1. Every product must have, price and quantity. 
# 2. Adda a method stock_value()
# 3. The method must return Stock Valuse = price * Quantity.
# 4. Display each product's information and stock valuse.



from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def stock_value(self) -> float:
        return self.price * self.quantity


products = [
    Product("Keyboard", 25.0, 10),
    Product("Mouse", 15.0, 20),
    Product("Monitor", 150.0, 4),
]

for product in products:
    print(
        f"{product.name} - Price: {product.price} - "
        f"Quantity: {product.quantity} - Value: {product.stock_value()}"
    )