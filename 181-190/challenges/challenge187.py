# Challenge 187 ; Extract nested JSON Data

# Requirements.
# Request the user records.
# Check the HTTP status
# Display the user's name and email
# display the city from the nested address
# Display the company name from the nested company dictionaries


import requests
 
url = "https://jsonplaceholder.typicode.com/users/2"
 
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
 
    user = response.json()
 
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
 

    print(f"City: {user['address']['city']}")
    print(f"Company: {user['company']['name']}")
 
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")