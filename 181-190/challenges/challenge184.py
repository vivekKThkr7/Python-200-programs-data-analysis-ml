# Challenge 184; Retrieve and Process Comments


import requests
 
url = "https://jsonplaceholder.typicode.com/posts/1/comments"
 
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # stop here if the status is bad
 
    comments = response.json()  # list of dictionaries
 
    print(f"Total comments: {len(comments)}")
 
    for comment in comments[:3]:
        print()  # blank line between comments for readability
        print(f"Comment ID: {comment['id']}")
        print(f"Name: {comment['name']}")
        print(f"Email: {comment['email']}")
 
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
 