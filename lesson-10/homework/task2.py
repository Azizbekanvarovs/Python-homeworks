import requests
import random

api_key = "035d764897e18aed0427e81dc15a6ce0"
genre_name = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")

# Step 1: Get genre IDs
genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
genre_response = requests.get(genre_url).json()
genres = genre_response['genres']

genre_id = None
for genre in genres:
    if genre['name'].lower() == genre_name.lower():
        genre_id = genre['id']
        break

if genre_id is None:
    print("Genre not found.")
else:
    # Step 2: Get movies from that genre
    discover_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}&sort_by=popularity.desc"
    movie_response = requests.get(discover_url).json()
    movies = movie_response['results']

    if movies:
        movie = random.choice(movies)
        print("Movie Recommendation:")
        print("Title:", movie['title'])
        print("Overview:", movie['overview'])
    else:
        print("No movies found in this genre.")