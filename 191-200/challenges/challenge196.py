# Grouping and analyzing data (Use pandas groupby() to answer business questions)
# Create a sales DataFrame with these columns:
# Product
# category
# region
# revenue

# This program must calcualte total revenue by category, total revenue by region, and identify which category generated the highest revenue.



import pandas as pd
 
df = pd.DataFrame({
    "product":  ["Laptop", "Phone", "Desk", "Chair", "Shirt", "Jeans"],
    "category": ["Electronics", "Electronics", "Furniture", "Furniture", "Clothing", "Clothing"],
    "region":   ["North", "South", "North", "South", "North", "South"],
    "revenue":  [1200, 800, 400, 300, 150, 200],
})
 
by_category = df.groupby("category")["revenue"].sum()
by_region = df.groupby("region")["revenue"].sum()
 
print("Revenue by category:\n", by_category)
print("\nRevenue by region:\n", by_region)
 
# idxmax() returns the LABEL (category name) with the biggest value
top = by_category.idxmax()
print(f"\nTop category: {top} ({by_category[top]})")
 