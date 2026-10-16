# Create a reusable function.

import requests


def fetch_post(post_id: int) -> dict:
    if post_id <= 0:
        raise ValueError("Post ID must be greater than 0.")

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def main() -> None:
    post_ids = [1, 2, 3]

    for post_id in post_ids:
        try:
            post = fetch_post(post_id)

            print("Post ID:", post["id"])
            print("Title:", post["title"])
            print()

        except ValueError as error:
            print("Invalid input:", error)

        except requests.exceptions.RequestException as error:
            print("Could not fetch post:", error)


if __name__ == "__main__":
    main()