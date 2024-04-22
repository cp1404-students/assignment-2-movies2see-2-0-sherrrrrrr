"""..."""


# TODO: Create your MovieCollection class in this file

import json
import csv
from movie import Movie

WATCHED_STATUS = 'w'
UNWATCHED_STATUS = 'u'


class Movie:
    def __init__(self, title, year, category, watched):
        self.title = title
        self.year = year
        self.category = category
        self.watched = watched


class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_number_of_unwatched_movies(self):
        return sum(1 for movie in self.movies if movie.status == UNWATCHED_STATUS)

    def get_number_of_watched_movies(self):
        return sum(1 for movie in self.movies if movie.status == WATCHED_STATUS)

    def load_movies_from_json(self, filename):
        try:
            with open(filename, mode='r') as file:
                movie_data = json.load(file)
                self.movies.extend(
                    Movie(data['title'], int(data['year']), data['category'], data['status'].lower() == 'w')
                    for data in movie_data
                )
        except FileNotFoundError:
            print(f"No existing file {filename}.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}.")

    def load_movies_from_csv(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                self.movies.extend(
                    Movie(title, int(year), category, status.lower() == 'w')
                    for title, year, category, status in reader
                )
        except FileNotFoundError:
            print(f"No existing file {filename}.")

    def save_movies_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump([movie.to_dict() for movie in self.movies], file, indent=4)

    def sort(self, key):
        self.movies.sort(key=lambda movie: (getattr(movie, key), movie.year if key == 'title' else movie.title))
