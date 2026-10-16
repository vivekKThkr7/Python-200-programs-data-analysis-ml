import requests

url = "https://jsonplaceholder.typicode.com/posts/999999"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    print("Post title:", data["title"])

except requests.exceptions.Timeout:
    print("The request timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the server.")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Other request error:", error)