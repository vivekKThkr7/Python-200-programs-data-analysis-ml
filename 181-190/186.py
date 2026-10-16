# Sending Data with a POST Request
# The HTTP POST method is commonly used to submit informatiob, such as a new post, registration, order, or form

import requests
url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Learning Python APIs",
    "body": "This Post was sent using Python.",
    "userID": 1
}

try:
    response = requests.post(
        url,
        json=new_post,
        timeout=10
    )

    response.raise_for_status()

    created_post = response.json()

    print("Post submitted successfullt.")
    print("Requested ID; ", created_post['id'])
    print("Title: ", created_post['title'])

except requests.exceptions.RequestException as error:
    print("Request Failed:", error)
    