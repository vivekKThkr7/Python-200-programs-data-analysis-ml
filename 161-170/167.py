# Save Date as JSON
# JSON is a common format for storing structured data. 

import json

expenses = [
    {"description": "Lunch", "amount": 25.5, "category": "Food"},
    {"description": "Taxi", "amount": 15, "category": "Travel"}
]

with open ("outputs/json/expenses.json", 'w') as file:
    json.dump(expenses, file, indent=4)

    print("Expenses Saved")


# This creates "outputs/json/expenses.json"  (the file will contain structured data)

# json.dump() : Converts python data into JSON and write it to the file. 

