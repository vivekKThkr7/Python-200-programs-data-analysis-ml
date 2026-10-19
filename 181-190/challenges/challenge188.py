# Challenge 188 ; Create a reusable API Function

# Requirements.
# Accept aa post ID as a parameter.
# Raise ValueError if the ID is zero or negative.
# build the endpoint URL using the supplied ID.
# Send a GET request with a timeout.
# Check the response status.
# return the parsed JSON dictionary
# Retrieve posts 1, 2 and 3 using a loop.
# Handle request error in the calling code. 

import requests

def fetch_post(post_id):   

    if post_id <= 0 :
        raise ValueError("Post ID must be a positive number.")

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


for post_id in [1, 2, 3]:
    try:
        post = fetch_post(post_id)

        print(f"ID : {post['id']} | Title : {post['title']}")

    except ValueError as error:
        print(f"Invalid ID: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request failed for post {post_id}: {error}")
 