"""..."""
# TODO: Copy your first assignment to this file, then update it to use Movie class

from movie import Movie
from moviecollection import MovieCollection
import csv

UNWATCHED = "u"
WATCHED = "w"


def main():
    print("Movies2See 1.0 - by Jiaxin Li")
    file_name = 'movies.csv'
    movies = load_movies(file_name)
    movies_sorted = []
    print(f"{len(movies)} movies loaded")

    while True:
        print("Menu")
        print("D - Display movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")

        choice = input("~ ").lower()

        if choice == 'd':
            movies_sorted = display_movies(movies)  # Store the sorted movies
        elif choice == 'a':
            add_movie(movies)
        elif choice == 'w':
            if movies_sorted:  # Ensure movies_sorted is not empty
                watch_movie(movies_sorted, movies)  # Pass the sorted movies
            else:
                print("Please display movies first.")
        elif choice == 'q':
            save_movies(file_name, movies)
            print(f"{len(movies)} movies saved to movies.csv")
            print("Have a nice day :)")
            return True
        else:
            print("Invalid menu choice")

    return False


def load_movies(file_name):
    movies = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            movies.append(row)
    return movies


def save_movies(file_name, movies):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Year', 'Category', 'Status'])
        writer.writerows(movies)


def display_movies(movies):
    watched_count = 0
    unwatched_count = 0
    movies_sorted = sorted(movies, key=lambda x: int(x[1]))

    max_title_len = max(len(movie[0]) for movie in movies_sorted)

    for i, movie in enumerate(movies_sorted):
        status = '*' if movie[3] == UNWATCHED else ''
        print(f"{i}. {status} {movie[0]:<{max_title_len}} - {movie[1]} ({movie[2]})")

        if movie[3] == UNWATCHED:
            unwatched_count += 1
        else:
            watched_count += 1

    print(f"{watched_count} movies watched, {unwatched_count} movies still to watch")
    return movies_sorted


def add_movie(movies):
    title = input("Title: ")

    while title.strip() == "":
        print("Input can not be blank")
        title = input("Title: ")

    while True:
        year = input("Year: ")
        try:
            year_int = int(year)  # Attempt to convert year to integer
            if year_int < 0:
                print("Number must be >= 0")
            else:
                break  # Exit the loop if year is a non-negative number
        except ValueError:
            print("Invalid input; enter a valid number")

    category = input("Category: ")
    while category.strip() == "":
        print("Input cannot be blank")
        category = input("Category: ")

    movies.append([title, year, category, UNWATCHED])
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(movies_sorted, movies_original):
    if not movies_sorted:
        print("No movies sorted. Please display movies first.")
        return
    unwatched_movies = [movie for movie in movies_sorted if movie[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return

    print("Enter the number of a movie to mark as watched:")
    choice = input().strip()

    try:
        choice = int(choice)

        if not 0 <= choice < len(movies_sorted):
            print("Invalid movie number")
            return

        selected_movie = movies_sorted[choice]
        for movie in movies_original:
            if movie[:3] == selected_movie[:3]:
                if movie[3] == UNWATCHED:
                    movie[3] = WATCHED
                    print(f"{movie[0]} from {movie[1]} watched")
                else:
                    print(f"You have already watched {movie[0]}")
                return

        print("Movie not found.")

    except ValueError:
        print("Invalid input; enter a valid number")


if __name__ == '__main__':
    while True:
        should_quit = main()
        if should_quit:
            break
