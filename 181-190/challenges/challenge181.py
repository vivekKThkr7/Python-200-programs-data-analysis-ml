# Challenge 181 : Fetch a Single Post

# Write a program that retrives POST number 2 from JSONPlaceholder.

# Requirements:
# Import requests
# Send GET request
# Parse the JSON response
# Display the post ID, title, and user ID.

import requests    

# The full address (URL) of post number 2
url = "https://jsonplaceholder.typicode.com/posts/2"

response = requests.get(url, timeout=10)

post = response.json()


print(f"Post ID: {post['id']}")
print(f"Title: {post['title']}")
print(f"user ID: {post['userId']}")