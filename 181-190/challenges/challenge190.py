# Challenge 190 ; Mini User Directory API

# Build a command-line application that retrieves and displays a user profile from JSONPlaceholder.

# STRUCTURE (one job per function):
#     fetch_user()   -> gets data from the API
#     display_user() -> shows data to the user
#     main()         -> coordinates input, calls, and error handling




import requests
 
BASE_URL = "https://jsonplaceholder.typicode.com/users"
 
 
def fetch_user(user_id):

    if user_id <= 0:
        raise ValueError("User ID must be a positive number.")
 
    response = requests.get(f"{BASE_URL}/{user_id}", timeout=10)
    response.raise_for_status()  # 404 -> HTTPError
    return response.json()
 
 
def display_user(user):
    """Print a formatted profile from a user dictionary."""
    print("\n----- USER PROFILE -----")
    print(f"Name: {user['name']}")
    print(f"Username: {user['username']}")
    print(f"Email: {user['email']}")
    print(f"City: {user['address']['city']}")
    print(f"Company: {user['company']['name']}")
 
 
def main():
    """Ask for an ID, fetch the user, display it, handle errors."""
    user_input = input("Enter user ID (1-10): ")
 
   
    try:
        user_id = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return  # stop; nothing to fetch
 
   
    try:
        user = fetch_user(user_id)
        display_user(user)
 
    except ValueError as error:
        
        print(f"Validation error: {error}")

    except requests.exceptions.HTTPError as error:

        if error.response is not None and error.response.status_code == 404:
            print("User not found.")
        else:
            print(f"The server returned an error: {error}")

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")

    except requests.exceptions.RequestException as error:
        print(f"A request error occurred: {error}")
 
 
# Execution guard: main() runs only when this file is run directly,
# not when it is imported into another program.
if __name__ == "__main__":
    main()