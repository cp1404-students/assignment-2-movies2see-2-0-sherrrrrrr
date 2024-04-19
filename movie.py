"""..."""


# TODO: Create your Movie class in this file


class Movie:
    def __init__(self, title, year, category, watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.watched = watched

    def mark_as_watched(self):
        self.watched = True

    def mark_as_unwatched(self):
        self.watched = False

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.category} Watched: {self.watched}"

class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_number_of_unwatched_movies(self):
        return sum(1 for movie in self.movies if not movie.watched)

    def get_number_of_watched_movies(self):
        return sum(1 for movie in self.movies if movie.watched)