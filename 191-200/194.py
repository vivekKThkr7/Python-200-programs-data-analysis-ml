# Reading and writing CSV (Comma-seperated Values) Data with pandas

import pandas as pd

data = {
    "product": ["Keyboard", "Mouse", "Chair"],
    "category": ["Electronics", "Electronics", "Furniture"],
    "revenue": [250, 150, 400]
}

df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv("sales.csv", index=False)

print("Sales data saved.")

# Read the data back from the CSV file
sales = pd.read_csv("sales.csv")

print("\nLoaded sales data:")
print(sales)

print("\nTotal revenue:", sales["revenue"].sum())