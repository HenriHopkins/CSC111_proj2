from typing import Union
from typing import Tuple
import csv
import networkx as nx
import get_user_input
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


def recommend_movies(user_movies, user_ratings, graph) -> list[str]:
    """Based on what the user has rated certain movies, a list of the titles of recommended movies
    is returned"""
    # this would be a good place to implement binary search or some other quick search method me thinks
    # how am I gonna do this
    # how calculate similarity score, do for each in list? then summ everything and return highest score?
    # Convert movie names to movie ids
    # user_movie_ids = []
    # for movie_name in user_movies:
    #     for movie_id, data in movies_data.items():
    #         if movie_name.lower() in data[0].lower():
    #             user_movie_ids.append(movie_id)
    #             break  # delete/fix probs
    #
    # # Calculate similarity scores
    # similarity_scores = {}
    # for movie_id in user_movie_ids:
    #     neighbors = graph.get_neighbors(movie_id)
    #     if neighbors:
    #         for neighbor_id in neighbors:
    #             if neighbor_id not in similarity_scores:
    #                 similarity_scores[neighbor_id] = 0
    #             similarity_scores[neighbor_id] += graph.get_weight(movie_id, neighbor_id)
    # pls fix
    user_movie_ids = []
    for movie_name in user_input_movies:
        for movie_id, data in movies_data.items():
            if movie_name.lower() in data[0].lower():
                user_movie_ids.append(movie_id)
                break  # WHAT PURPOSE DOES THIS SERVE LOL

    similarity_scores = {}
    for movie_id in user_movie_ids:
        for neighbor_id in G.neighbours(movie_id):
            if neighbor_id not in similarity_scores:
                similarity_scores[neighbor_id] = 0
            similarity_scores[neighbor_id] += G[movie_id][neighbor_id]['weight']

    sorted_movies = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)  # do I do quicksort here? idek

    recommended_movies = [(movie_id, movies_data[movie_id][0]) for movie_id, _ in sorted_movies if
                          movie_id not in user_movie_ids]

    return recommended_movies


def returned_movies(recommended_movies: list, G: nx.Graph()) -> None:
    """Recursive function that lets the user pick ____"""
    i = input("Input the movie you want to learn about: ")
    if i in recommended_movies:
        inp = input("Which of the following would you like to know about the movie: ")
        if inp.upper() == "GENRE":
            return ___
        elif inp.upper() == "RATING":
            return ___
        elif inp.upper() == "CAST":
            return ___
        else:
            "Not a valid input, try again"  # how the fuck do I make this recursive lol
    if i.upper() == "EXIT":
        return


if __name__ == "__main__":
    # Read data from CSV files
    movies_data, genres_data, actors_data = read_csv_files("files/movies.csv", "files/genres.csv", "files/actors.csv")

    # Construct weighted graph
    G = make_graph.construct_graph(movies_data, genres_data, actors_data)

    # Get user input
    user_input_movies, user_ratings = get_user_input.decide_user_input(movies_data)

    # Recommend movies
    recommended_movies = recommend_movies(user_input_movies, user_ratings, movies_data, graph)
    print("Recommended Movies:")
    for movie_id, movie_name in recommended_movies:
        print(movie_name)
    returned_movies(recommended_movies)
