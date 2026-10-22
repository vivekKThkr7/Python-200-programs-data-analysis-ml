# Grouping and Analysing Data

# groupby()  ->> group redcords according to a particular column and then lets you calculate a stastic for each group.


import pandas as pd

data = {
    "product": ["Keyboard", "Mouse", "Chair", "Desk", "Monitor"],
    "category": [
        "Electronics",
        "Electronics",
        "Furniture",
        "Furniture",
        "Electronics"
    ],
    "revenue": [250, 150, 400, 200, 300]
}

df = pd.DataFrame(data)

summary = df.groupby("category")["revenue"].agg(
    ["sum", "mean"]
)

print("Revenue summary by category:")
print(summary)