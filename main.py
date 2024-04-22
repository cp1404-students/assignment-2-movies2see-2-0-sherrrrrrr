"""
Name: JiaxinLi
Date: 19/04/2024
Brief Project Description: The assessment involves the development of a movie management
      system that includes a console program and a GUI program using the Kivy framework.
      The objective is to create a Movie class with attributes and methods to handle movie
      data, a MovieCollection class to manage a list of Movie objects, and a GUI interface
      for users to interact with the movie database.
GitHub URL: https://github.com/cp1404-students/assignment-2-movies2see-2-0-sherrrrrrr
"""
# TODO: Create your main program in this file, using the Movies2SeeApp class
from movie import Movie
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from functools import partial
from moviecollection import MovieCollection


class MovieListApp(App):
    def build(self):
        self.title = "Movies2See"
        self.root = Builder.load_file('app.kv')
        self.movie_collection = MovieCollection()
        self.load_movies('movies.json')
        self.display_movies()
        return self.root

    def load_movies(self, filename):
        with open(filename, 'r') as file:
            movie_data = json.load(file)
        for movie_dict in movie_data:
            movie = Movie(**movie_dict)
            self.movie_collection.add_movie(movie)

    def display_movies(self):
        movie_layout = self.root.ids['movies_container']
        movie_layout.clear_widgets()

        for movie in self.movie_collection.movies:
            button_color = (0, 0, 1, 1) if movie.watched else (1, 0, 0, 1)
            button = Button(text=movie.title, background_color=button_color)
            button.bind(on_release=partial(self.toggle_watched_status, movie))
            movie_layout.add_widget(button)
        self.update_status()

    def toggle_watched_status(self, movie, button):
        movie.watched = not movie.watched
        self.display_movies()

    def add_movie(self):
        title_input = self.root.ids.title_input.text
        year_input = self.root.ids.year_input.text
        category_input = self.root.ids.category_input.text
        error_label = self.root.ids.error_label

        if not title_input or not year_input.isdigit() or not category_input:
            error_label.text = "All fields must be filled out and year must be a number."
            return

        movie = Movie(title_input, int(year_input), category_input)
        self.movie_collection.add_movie(movie)
        self.display_movies()
        self.clear_input_fields()

    def clear_input_fields(self):
        self.root.ids.title_input.text = ''
        self.root.ids.year_input.text = ''
        self.root.ids.category_input.text = ''
        self.root.ids.error_label.text = ''

    def update_status(self):
        watched = self.movie_collection.get_number_of_watched_movies()
        unwatched = self.movie_collection.get_number_of_unwatched_movies()
        self.root.ids.status_label.text = f"Watched: {watched} Unwatched: {unwatched}"

    def on_stop(self):
        movie_data = self.movie_collection.get_movies_as_dicts()
        with open('movies.json', 'w') as file:
            json.dump(movie_data, file, indent=4)


if __name__ == '__main__':
    MovieListApp().run()