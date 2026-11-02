# Cleaning missing and duplicate data 
# Create an inventory DataFrame containing at least six rows,
# at least one exact duplicate product record, one missing price,
# and a quantity column.

# This program should report the number of duplicate rows and missing values, remove genuine duplicate records, fill the missing price with the median price, create a stock_value column using price multiplied by quantity, and print the cleaned DataFrame.

# .duplicated(), .drop_duplicates(), .isna().sum() and .fillna()

import pandas as pd
 
df = pd.DataFrame({
    "product":  ["Pen", "Notebook", "Bag", "Pen", "Ruler", "Bag", "Marker"],
    "price":    [2.0,    5.0,        30.0,  2.0,   None,    30.0,  4.0],
    "quantity": [20,     10,         3,     20,    15,      5,     8],
})


# Row 3 = exact copy of row 0 (true duplicate -> remove)
# Row 5 = Bag again but quantity 5 (legit separate record -> keep)
# Ruler has a missing price
 
print("Duplicate rows:", df.duplicated().sum())
print("Missing values:\n", df.isna().sum())
 
df = df.drop_duplicates()   # removes only identical rows
 
median_price = df["price"].median()     # median ignores the NaN
df["price"] = df["price"].fillna(median_price)
 
df["stock_value"] = df["price"] * df["quantity"]
 
print("\nCleaned DataFrame:")
print(df)
 