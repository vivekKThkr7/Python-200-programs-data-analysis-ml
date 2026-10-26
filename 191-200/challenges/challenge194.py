# reading and writing CSV data
# Caculate revenue for each product, save the DataFrame to challenge_sales.csv, read the file into a new DataFrame, and calculate total revenue from the loaded data. 

import pandas as pd
 
df = pd.DataFrame({
    "Product": ["Pen", "Notebook", "Bag"],
    "Quantity": [20, 10, 3],
    "Unit price": [2, 5, 30],
})
 
df["Revenue"] = df["Quantity"] * df["Unit price"]   # per-product revenue
 
# index=False stops pandas writing the row numbers into the file
df.to_csv("challenge194_sales.csv", index=False)
 
# Read the file into a NEW DataFrame (proves the save worked)
loaded = pd.read_csv("challenge194_sales.csv")
print(loaded)
print("Total revenue:", loaded["Revenue"].sum())    # 180
 