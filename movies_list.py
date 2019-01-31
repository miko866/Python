
movies = []

def menu():
    user_input = input("Enter [a] to add a movie, [l] to see your movies, [f] to find a movie, and [q] to quit.\n-> ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movies()
        else:
            print("Invalid input!")

        user_input = input(
            "\nEnter [a] to add a movie, [l] to see your movies, [f] to find a movie, and [q] to quit.\n-> ")


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie directors: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movies_details(movie)


def show_movies_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movies():
    find_by = input("What property of the movie are you looking for? ") # year, name or director
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found 


menu()
