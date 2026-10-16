# Filtering API results with Query parameters.


import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    'userID': 1
}

response = requests.get(url, params=params, timeout = 10)
response.raise_for_status()

posts = response.json()

print("Total posts found: ", len(posts))
print()

for post in posts[:3]:
    print(f"Post ID: {post['id']}")
    print(f"Title: {post['title']}")
    print()
