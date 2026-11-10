# API Requests Practice

Small Python project practicing the `requests` library against two public APIs:
[JSONPlaceholder](https://jsonplaceholder.typicode.com/) and [OMDB](http://www.omdbapi.com/).

## Tasks

| # | Task | Method |
|---|------|--------|
| 1 | Fetch posts, print status code and first post's title | `requests.get()` |
| 2 | Create a post, print status code and returned JSON | `requests.post()` |
| 3 | Fetch users, print usernames whose email ends in `.org` | `requests.get()` + `.json()` |
| 4 | Search OMDB for "Avengers", print total results | `requests.get(params={...})` |

## Setup

```bash
git clone <your-repo-url>
cd api-requests-practice
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python api_tasks.py
```

### OMDB API key

The script uses the `demo` key by default, which OMDB often rejects. Get a free key at
[omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx) and set it as an environment variable:

```bash
export OMDB_API_KEY=your_key_here      # Windows (PowerShell): $env:OMDB_API_KEY="your_key_here"
python api_tasks.py
```

## Notes

- JSONPlaceholder fakes write operations: the POST in task 2 returns status `201` and an `id` of `101`, but nothing is actually saved.
- Never commit a real API key. Keep it in an environment variable.
