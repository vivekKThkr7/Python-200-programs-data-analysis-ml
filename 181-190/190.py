# Mini Project: User Directory API
# We will create a small command-line application that ask for a user ID, retrieves that user's profile, and display thier details.
# This Project will show: GET request, Functions, Type hints, JSON parsing, Nested Dictionaries, input Validateion, Exception handling

import requests


def fetch_user(user_id: int) -> dict:
    if user_id <=0:
        raise ValueError("User ID must ")