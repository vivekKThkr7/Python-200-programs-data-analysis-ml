# Cleaning Missing and Duplicate Data 

# A CSV file or database export might contain missing prices, blank names, duplicate transactions, or incorrect values. 

# Data cleaning means identifying and handling these problems before aanalysing the data. 

import pandas as pd

data = {
    "product": ["Keyboard", "Mouse", "Mouse", "Monitor"],
    "price": [25, None, None, 150],
    "category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics"
    ]
}

df = pd.DataFrame(data)

print("Original data:")
print(df)

print("\nMissing values before cleaning:")
print(df.isna().sum())

# Replace missing prices with the median price
median_price = df["price"].median()
df["price"] = df["price"].fillna(median_price)

# Remove rows that are exact duplicates
df = df.drop_duplicates()

print("\nCleaned data:")
print(df)

print("\nMissing values after cleaning:")
print(df.isna().sum())