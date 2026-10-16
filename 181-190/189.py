# Saving API Data into a JSON File


import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

try:
    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    posts = response.json()

    # Save the API data locally
    with open("user1_posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)

    print("API data saved successfully.")

    # Read the saved data
    with open("user1_posts.json", "r", encoding="utf-8") as file:
        saved_posts = json.load(file)

    print("Posts saved:", len(saved_posts))

    if saved_posts:
        print("First post title:", saved_posts[0]["title"])

except requests.exceptions.RequestException as error:
    print("API request failed:", error)

except (OSError, json.JSONDecodeError) as error:
    print("File operation failed:", error)