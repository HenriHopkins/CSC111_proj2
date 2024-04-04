from typing import Union
from typing import Tuple
import csv
import networkx as nx
import get_user_input
import get_movies
import make_graph


def binary_search(lst: Union[list[int], list[float]], target: Union[int, float]):  # check if this implementation good
    """Given a list with either float or integer data, perform a binary search"""
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = lst[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main_menu(run_once: bool):
    """Main menu to the program, lets the user input their preferences"""
    if not run_once:
        k = 0
        try:
            k = int(input("Enter how many movies you'd like in the data set"))
        except ValueError:
            print("Invalid input")
            main_menu(False)
        movies_data, genres_data, actors_data = make_graph.read_csv_files_small("files/movies.csv", "files/genres.csv",
                                                                                "files/actors.csv", k)
        sorted_movies = sorted(movies_data.items(), key=lambda y: y[1])


if __name__ == "__main__":
    main_menu(False)
    # Read data from CSV files
    # movies_data, genres_data, actors_data = make_graph.read_csv_files("files/movies.csv", "files/genres.csv", "files/actors.csv")
    movies_data, genres_data, actors_data = make_graph.read_csv_files_small("files/movies.csv", "files/genres.csv",
                                                                            "files/actors.csv", 100)
    # sort using fastest sort we learned (in make graph method), makes binary search easy af
    # Construct weighted graph
    G = make_graph.construct_graph(movies_data, genres_data, actors_data)
    # G = make_graph.fast_one("files/movies.csv", "files/genres.csv", "files/actors.csv")
    # Get user input
    user_input_movies, user_ratings = get_user_input.decide_user_input(movies_data)  # fix this I beg
    # # Recommend movies
    recommended_movies = get_movies.recommend_movies(user_input_movies, user_ratings, movies_data, G)
    rm = [x[1] for x in recommended_movies]  # this is a list of movies for some reason idek
    for x in rm:  # also why the fuck is this a list of lists, pls fix
        print(rm)
    h = get_movies.returned_movies(rm, genres_data, actors_data, movies_data)
    print(h) # make it so that it iterates through the list and prints basically
    # print("Recommended Movies:")
    # for movie_id, movie_name in recommended_movies:
    #     print(movie_name)
    # returned_movies(recommended_movies)
