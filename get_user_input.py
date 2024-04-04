import csv
import networkx as nx
from typing import Tuple
import get_movies


def get_user_input_direct(movies_data: dict) -> Tuple[list, list]:
    """Obtain user input of their seen movies and associated ratings. Return two lists, one containing movie titles,
    and the other containing movie ratings. Take a list of known movies as function input and check that the user inputs
    a valid title and Letterboxd rating"""
    # adjust this function to take a .csv of seen movies from the user
    # user_input_movies = []
    # user_ratings = []
    # while len(user_input_movies) < 3: # idk what the minimum # of movies should be.
    #     movie_name = input("Enter a movie title: ")
    #     movie_id = None
    #     for id, data in movies_data.items():
    #         if movie_name.lower() in data[0].lower(): # binary search here instead?
    #             movie_id = id
    #             break
    #     if movie_id is None:
    #         print("Movie not found. Please enter a valid movie title.")
    #         continue
    #
    #     rating = None
    #     while rating is None:
    #         try:
    #             rating = float(input("Rate the movie (0.5 to 5): "))
    #             if rating < 0.5 or rating > 5:
    #                 print("Rating must be between 0.5 and 5.")
    #                 rating = None
    #         except ValueError:
    #             print("Invalid input. Please enter a valid rating.")
    #
    #     user_input_movies.append(movie_name)
    #     user_ratings.append(rating)
    #
    # return user_input_movies, user_ratings
    user_inputs = []
    ratings = []
    # sorted_movies = sorted(movies_data.items(), key=lambda y: y[1])
    print("Input 'DONE' as a movie title to stop entering things")
    ans = ''
    while not ans.upper() == 'DONE':
        ans = input("Enter a movie title: ")
        user_inputs.append(ans)
        if not ans.upper() == 'DONE':
            ans = input("Enter the Letterboxd rating: ")
            ratings.append(float(ans))
    if len(user_inputs) > len(ratings):
        user_inputs = user_inputs[:len(user_inputs) - 1]
    elif len(user_inputs) < len(ratings):   # can probs delete, or adjust to prevent float(ans) error (try, except?)
        ratings = ratings[:len(ratings) - 1]






    # ans = ''
    # print("ENTER 'DONE' TO STOP INPUTTING THINGS")
    # while not ans.upper() == 'DONE':
    #     ans = input("Enter a move title: ")

        # b = get_movies.binary_search_movie_id(sorted_movies, ans)
        # if b == -1:
        #     print("Not a valid title")  # do something to loop it
        # else:
        #     user_inputs.append(ans)
        # ans
        #
        # if len(user_inputs) > len(ratings):
        #     user_inputs.remove_index # do smth to remove index idfk lol

    # while len(user_inputs) < 3:
    #     name = input("Enter a movie title: ")
    #     input_id = None
    #     for id, data in movies_data.items():
    #         if name.lower() in data[0].lower():
    #             input_id = id
    #             break
    #     if input_id is None:
    #         print("Movie not found. Please enter a valid movie title.")
    #         continue
    #     rating = None
    #     while rating is None:
    #         try:
    #             rating = float(input("Rate the movie (0.5 to 5): "))
    #             if rating < 0.5 or rating > 5:
    #                 print("Rating must be between 0.5 and 5.")
    #                 rating = None
    #         except ValueError:
    #             print("Invalid input. Please enter a valid rating.")
    #
    #     user_inputs.append(name)
    #     ratings.append(rating)

    return user_inputs, ratings


def get_user_input_csv(movies_data: dict, user_file: str) -> Tuple[list, list]:
    """Returns two lists by reading a .csv file: the movie titles of user inputs, and the ratings of the
    associated movie.

    Preconditions:
        -if user_file is a valid path to a file, the file is a .csv file that has exactly two columns"""
    titles, ratings = [], []
    c = 0
    sorted_movies = sorted(movies_data.items(), key=lambda y: y[1])  # sort movies_data for binary search, maybe move outside fn scope (main)
    with open(user_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for title, rating in reader:
            c += 1
            if get_movies.binary_search_movie_id(sorted_movies, title) == -1:
                print(f'There was an invalid title at line {c}')
            if float(rating) not in {0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0}:
                print(f'There was an invalid rating at line {c}')
            else:
                titles.append(title)
                ratings.append(rating)
    return titles, ratings  # do I need to check if user data is valid?? idek


def decide_user_input(movies_data: dict) -> Tuple[list, list]:
    """hjhj"""
    i = input("Enter 1 you import your data from a .csv file, enter 2 to type it in: ")
    if i == '1':
        try:
            user_file = input("Enter the directory to your .csv file (e.g. files/test.csv): ")
            return get_user_input_csv(movies_data, "files/test.csv")
        except FileNotFoundError:
            print("The specified file was not found")
            valid_input = True  # delete these?
    elif i == '2':
        valid_input = True
        return get_user_input_direct(movies_data)
    else:
        print("Invalid input. Try again")
        return decide_user_input(movies_data)
