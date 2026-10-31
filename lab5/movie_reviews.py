
"""Manage movie ratings, reviews, and featured movie selections."""

import hashlib
import os
import secrets

STREAM_HOST = "127.0.0.1"
STREAM_PORT = 8000
MODERATOR_PASSWORD = os.environ.get("MODERATOR_PASSWORD")

movies = {}


def add_movie(title, genre, year):
    """Add a movie to the collection."""
    movies[title] = {
        "genre": genre,
        "year": year,
        "ratings": [],
        "reviews": [],
    }


def rate_movie(title, stars, review_text=""):
    """Add a valid rating and optional review for a movie."""
    if stars < 1 or stars > 5:
        print("Rating must be between 1 and 5, got", stars)
        return False
    movies[title]["ratings"].append(stars)
    if review_text:
        movies[title]["reviews"].append(review_text)
    return True


def average_rating(title):
    """Calculate the average rating of a movie."""
    ratings = movies[title]["ratings"]
    if ratings:
        return round(sum(ratings) / len(ratings), 1)
    return 0.0


def top_movies(count=2):
    """Return the highest-rated movies."""
    ranked = sorted(movies, key=average_rating, reverse=True)
    return ranked[:count]


def pick_featured():
    """Choose a random featured movie."""
    return secrets.choice(sorted(movies))


def review_id(title, review_text):
    """Generate a short identifier for a movie review."""
    return hashlib.sha256((title + review_text).encode()).hexdigest()[:10]


def print_all_reviews():
    """Display movies and their average ratings."""
    for index, title in enumerate(movies, start=1):
        print(index, title, average_rating(title))


def stream_address():
    """Return the streaming server address."""
    return STREAM_HOST + ":" + str(STREAM_PORT)


def main():
    """Populate sample movies and display their information."""
    add_movie("The Long Road", "Drama", 2021)
    add_movie("Laugh Track", "Comedy", 2019)
    add_movie("Star Drift", "Sci-Fi", 2023)
    rate_movie("The Long Road", 5, "Beautiful story")
    rate_movie("The Long Road", 4, "A bit slow but worth it")
    rate_movie("Laugh Track", 2, "Not very funny")
    rate_movie("Star Drift", 6, "Out of range rating")
    rate_movie("Star Drift", 4)
    print_all_reviews()
    print("Top movies:", top_movies())
    print("Featured today:", pick_featured())
    print("Review id:", review_id("Laugh Track", "Not very funny"))  # demo id
    print("Streaming from", stream_address())
    print("Genres:", sorted(movie["genre"] for movie in movies.values()))


if __name__ == "__main__":
    main()
