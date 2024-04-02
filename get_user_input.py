import csv
import networkx as nx
from typing import Tuple


def get_user_input_direct(movies_data):
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
    while len(user_inputs) < 3:
        name = input("Enter a movie title: ")
        input_id = None
        for id, data in movies_data.items():
            if name.lower() in data[0].lower():
                input_id = id
                break
        if input_id is None:
            print("Movie not found. Please enter a valid movie title.")
            continue
        rating = None
        while rating is None:
            try:
                rating = float(input("Rate the movie (0.5 to 5): "))
                if rating < 0.5 or rating > 5:
                    print("Rating must be between 0.5 and 5.")
                    rating = None
            except ValueError:
                print("Invalid input. Please enter a valid rating.")

        user_inputs.append(name)
        ratings.append(rating)

    return user_inputs, ratings


def get_user_input_csv(movies_data: list, user_file: str):
    """
    """
    # user_input_movies = []
    # user_ratings = []
    # c = 1
    # with open(user_file, 'r') as file:
    #     reader = csv.reader(file)
    #     next(reader)
    #     for title, rating in reader:
    #         # insert code to check if movie is valid with ID
    #         if rating < 0.5 or rating > 5:
    #             print(f"You have an invalid rating at line {c}")
    #         else:
    #             user_input_movies.append(title)
    #             user_ratings.append(rating)
    #         c += 1
    # return user_input_movies, user_ratings
    data = {}
    with open(user_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data[row[0]] = row[1:]
    return data


def decide_user_input(movies_data: list) -> Tuple[list, list]:
    """hjhj"""
    i = input("Enter 1 you import your data from a .csv file, enter 2 to type it in: ")
    if i == '1':
        try:
            user_file = input("Enter the directory to your .csv file")
            return get_user_input_csv(movies_data, user_file)
        except FileNotFoundError:
            print("The specified file was not found")
            valid_input = True
    elif i == '2':
        valid_input = True
        return get_user_input_direct(movies_data)
    else:
        print("Invalid input. Try again")
        return decide_user_input(movies_data)
