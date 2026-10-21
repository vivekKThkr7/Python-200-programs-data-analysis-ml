# Pandas DataFrames
# Pands is a Python library used to analuse structured data, such as spreadsheets, sales report, and employee records.

import pandas as pd

data = {
    "product" : ["keyboard", "Mouse", "Monitor"],
    "price" : [25, 15, 150],
    "quantity" : [10, 5, 3]
}

df = pd.DataFrame(data)

df["stock_value"] = df["price"] * df["quantity"]   # Converts the dictionary into a table.

print("Complete inventory: ")
print(df)

print("\nProducts with quantity below 10: ")
low_stock = df[df["quantity"] < 10]
print(low_stock)


