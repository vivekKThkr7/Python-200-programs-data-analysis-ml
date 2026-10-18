# Mini Project: User Directory API
# We will create a small command-line application that ask for a user ID, retrieves that user's profile, and display thier details.
# This Project will show: GET request, Functions, Type hints, JSON parsing, Nested Dictionaries, input Validateion, Exception handling


import requests


def fetch_user(user_id: int) -> dict:
    if user_id <= 0:
        raise ValueError("User ID must be greater than 0.")

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def display_user(user: dict) -> None:
    print("\n----- USER PROFILE -----")
    print("Name:", user["name"])
    print("Username:", user["username"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
    print("Company:", user["company"]["name"])


def main() -> None:
    try:
        user_id = int(input("Enter user ID (1-10): "))

        user = fetch_user(user_id)

        display_user(user)

    except ValueError as error:
        print("Invalid input:", error)

    except requests.exceptions.HTTPError as error:
        if error.response is not None and error.response.status_code == 404:
            print("User not found.")
        else:
            print("The server returned an HTTP error.")

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")

    except requests.exceptions.RequestException as error:
        print("Could not retrieve user:", error)


if __name__ == "__main__":
    main()
