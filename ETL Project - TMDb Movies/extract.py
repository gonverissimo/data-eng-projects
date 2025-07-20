import requests
import os
from dotenv import load_dotenv

load_dotenv("key.env")
API_KEY = os.getenv("TMDB_API_KEY")

def fetch_popular_movies(page=1):
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {"api_key": API_KEY, "language": "en-US", "page": page}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data["results"]
