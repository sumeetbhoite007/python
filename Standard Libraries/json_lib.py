import json
from pathlib import Path

movies = [
    {"id": 1, "title": "horror", "rating": 5},
    {"id": 2, "title": "horror2", "rating": 4},
    {"id": 3, "title": "horror3", "rating": 3}
]

data = json.dumps(movies)  # Pretty print JSON
Path("movies.json").write_text(data)