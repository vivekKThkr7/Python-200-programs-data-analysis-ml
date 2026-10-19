# Challenge 189 ; Save API Data to a JSON File

# Retrieve posts belonging to user 1 and save the response to user_posts.json.

# Requirements
# 1. Retrieve the posts using the userId query parameter.
# 2. Check the HTTP response.
# 3. Parse the JSON data.
# 4. Save the data to a JSON file using json.dump().
# 5. Read the saved file with json.load().
# 6. Display the number of saved records.
# 7. Display the title of the first saved post.
# 8. Handle request errors and file errors.



import json
import requests
 
url = "https://jsonplaceholder.typicode.com/posts"
filename = "user_posts.json"
 
try:
    
    response = requests.get(url, params={"userId": 1}, timeout=10)
    response.raise_for_status()
    posts = response.json()  # list of dictionaries from the API
 
    
    # 'with' closes the file automatically, even if an error occurs
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)  # indent=4 -> readable file
    print("API data saved successfully.")
 
    
    with open(filename, "r", encoding="utf-8") as file:
        saved_posts = json.load(file)  # data loaded from the file
 
    print(f"Posts saved: {len(saved_posts)}")
    print(f"First post title: {saved_posts[0]['title']}")
 
except requests.exceptions.RequestException as error:
    print(f"API request failed: {error}")
    
except OSError as error:
    print(f"File error: {error}")

except json.JSONDecodeError as error:
    print(f"The saved file contained invalid JSON: {error}")
 