# Working with Nested JSON


import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)
response.raise_for_status()

user = response.json()

print("Name:", user["name"])
print("Email:", user["email"])

print("City:", user["address"]["city"])
print("Company:", user["company"]["name"])