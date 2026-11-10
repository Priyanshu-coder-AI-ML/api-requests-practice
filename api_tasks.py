"""Practice tasks using the `requests` library with JSONPlaceholder and OMDB."""

import os

import requests

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com"
OMDB_URL = "http://www.omdbapi.com/"
# Set your own key with: export OMDB_API_KEY=your_key  (falls back to 'demo')
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "demo")
TIMEOUT = 10


def task1_get_posts():
    """GET all posts; print the status code and the first post's title."""
    print("--- Task 1: GET posts ---")
    response = requests.get(f"{JSONPLACEHOLDER_URL}/posts", timeout=TIMEOUT)
    print("Status code:", response.status_code)
    response.raise_for_status()
    posts = response.json()
    print("First post title:", posts[0]["title"])


def task2_create_post():
    """POST a new post; print the status code and the returned JSON."""
    print("\n--- Task 2: POST a new post ---")
    payload = {
        "title": "My First Post",
        "body": "Hello from Python!",
        "userId": 101,
    }
    response = requests.post(
        f"{JSONPLACEHOLDER_URL}/posts", json=payload, timeout=TIMEOUT
    )
    print("Status code:", response.status_code)
    print("Returned JSON:", response.json())


def task3_org_users():
    """GET users; print usernames whose email ends with '.org'."""
    print("\n--- Task 3: Users with .org emails ---")
    response = requests.get(f"{JSONPLACEHOLDER_URL}/users", timeout=TIMEOUT)
    response.raise_for_status()
    for user in response.json():
        if user["email"].lower().endswith(".org"):
            print(user["username"])


def task4_omdb_search():
    """Search OMDB for 'Avengers'; print the total number of results."""
    print("\n--- Task 4: OMDB search ---")
    params = {"apikey": OMDB_API_KEY, "s": "Avengers"}
    response = requests.get(OMDB_URL, params=params, timeout=TIMEOUT)
    data = response.json()
    if data.get("Response") == "True":
        print("Total results found:", data["totalResults"])
    else:
        # The 'demo' key is often rejected; show the reason instead of crashing.
        print("OMDB returned an error:", data.get("Error"))


def main():
    for task in (task1_get_posts, task2_create_post, task3_org_users, task4_omdb_search):
        try:
            task()
        except requests.RequestException as exc:
            print(f"Request failed in {task.__name__}: {exc}")


if __name__ == "__main__":
    main()
