# Challenge 186 ; Submit a New Post
# Submit this dictionary to the JSONPlaceholderposts endpoint:

# new = {
#     "title" : "Python API Practice",
#     "body": "I am learning how to send data with Python.", 
#     "userId" : 1
# }

# Requirements
# 1. use " request.post() "
# 2. Send the dictionary through the json argument 
# 3. check the HTTP response
# 4. parse the returned ID and title.
# 5. Display the returned ID and title.
# 6. Handle request-related exceptions


import requests

url = "https://jsonplaceholder.typicode.com/posts"

new = {
    "title" : "Python API Practice",
    "body": "I am learning how to send data with Python.", 
    "userId" : 1,
}


try:
   
    response = requests.post(url, json=new, timeout=10)
 
    
    response.raise_for_status()
 
    created_post = response.json()  # the server's reply as a dictionary
 
    print("Post submitted successfully.")
    print(f"Title: {created_post['title']}")
    print(f"Returned ID: {created_post['id']}")
 
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
 