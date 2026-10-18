# Challenge 183 Filter post Using Query Parameters

# Create a program that asks the user for a user ID and retrives posts belonging to that user.
# Requirements:
# Ask ther user for an ID
# Convert the input into an integer.
# Send a GET requeset to /posts using the userId query parameter
# Display the number of posts returned
# Display the ID and title of every returned post.
# handle invalid integer without crashing.


import requests

url = "https://jsonplaceholder.typicode.com/posts"

user_input = input("Enter user ID: ")

try:
    user_id = int(user_input)   # raises ValueError for things like "abc"

except ValueError:
    print("Invalid input. Please enter a whole number.")

else:   # 'else' runs only if the conversion workd
    try:
        # params builds the query string for us: ...?userId=<user_id>

        response = requests.get(url, params={"userId": user_id}, timeout=10)
        response.raise_for_status()

        posts = response.json() 

        print(f"Total posts found: {len(posts)}")


        for post in posts:
            print(f"ID: {post['id']} | Tilte: {post['title']}")

    except requests.exceptions.RequestException as error:
        print("Request failed: {error}")