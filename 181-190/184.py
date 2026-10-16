# Reading and writing Data Returned by an API


import requests

url = "https://jsonplaceholder.typicode.com/posts/1/comments"

response = requests.get(url, timeout=10)
response.raise_for_status()

comments = response.json()

print("Total comments:", len(comments))
print()

for comment in comments[:3]:
    print("Comment ID:", comment["id"])
    print("Name:", comment["name"])
    print("Email:", comment["email"])
    print()
