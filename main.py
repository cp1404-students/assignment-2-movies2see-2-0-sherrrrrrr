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

#from kivy.app import App
from moviecollection import MovieCollection

def main():
    file_name = 'movie.csv'
    movie_collection = MovieCollection()
    movie_collection.load_movies_from_csv(file_name)

    for movie in movie_collection.movies:
        print(movie)

if __name__ == "__main__":
    main()

