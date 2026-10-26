# pandas DataFrame ; Build and analyze an employee table. 
# create the DataFrame, add an annual_salary column, display only employees earning at least 5000 per month, and calculate the total monthly salary.

import pandas as pd

df = pd.DataFrame({
    "Employee" : ["Asha", "Ravi", "Mina", "Omat"],
    "Department" : ["IT", "HR", "IT", "Sales"],
    "Monthly salary" : [5000, 4200, 6500, 5800],
})

# new column: calculated for every row at once. 
df["annual_salary"] = df["Monthly salary"] * 12

print("Full table:")
print(df)

# Filter: keep only rows where the condition is True
print("\nEarning at least 5000 per month: ")
print(df[df["Monthly salary"] >= 5000])

print("\nTotal mpnthly salary: ", df["Monthly salary"].sum())

