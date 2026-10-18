# Check the HTTP status
# Write a program that retrives an existing post check the response.
# Requirements
# Retrieve post 1
# Display the status code.
# Call raise_for_status()
# If the request succesds, display the title.
# handle request-related exceptions.

# Extra task: Change the URL to a nonexistent post and observe how your exception handling responds.


import requests

post_id = 1 

url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

try:
    response = requests.get(url, timeout=10)

    print(f"Status code: {response.status_code}")   # Show the numeric status code (200 means ok)

    response.raise_for_status()

    post = response.json()
    print(f"Post title: {post['title']}")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")

    

