# # Our file realistic prgogram

# from pathlib import Path

# file_path = Path("notes.txt")

# if file_path.exists():
#     print("File already exists.")
# else:
#     file_path.write_text("Python Developer Notes\n", encoding="utf-8")
#     print("File created.")
    


# Cleaner Data Objects with dataclass

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int


product = Product("Keyboard", 25.5, 10)

print(product)
print(product.name)
print(product.price)
print(product.quantity)

