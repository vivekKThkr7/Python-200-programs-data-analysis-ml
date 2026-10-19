# Challlenge 185 ; Handle API Faliures
# Request a post that doesn't exist, such as 9999999
# Requirements.
# 1. Send a GET request with a timeout.
# 2. Check the HTTP response using "raise_for-status()"
# 3. handle an HTTO error seperately from a timout and connection faliure
# 4. display an appropriate message instead of letting a request error terminate the program unexceptedly.


import requests
 

url = "https://jsonplaceholder.typicode.com/posts/999999"
 
try:
  
    response = requests.get(url, timeout=5)
 
    
    response.raise_for_status()   # Converts the 404 into an HTTPError exception
 
    print(response.json())
 
except requests.exceptions.HTTPError:
    print("The requested post could not be retrieved.")

except requests.exceptions.Timeout:
    print("The request timed out. Please try again later.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the server. Check your internet connection.")
    
except requests.exceptions.RequestException as error:
    print(f"An unexpected request error occurred: {error}")
 