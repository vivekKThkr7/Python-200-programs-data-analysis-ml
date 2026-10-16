import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

data = response.json()

print("Post ID:", data["id"])
print("Title:", data["title"])
print("User ID:", data["userId"])