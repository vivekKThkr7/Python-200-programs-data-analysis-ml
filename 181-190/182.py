import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)

    print("Status code: ", response.status_code)

    response.raise_for_status()

    data = response.json()

    print("Post title: ", data['title'])

except requests.exceptions.RequestException as error:
    print("Request Failed: ", error)
    