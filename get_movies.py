from typing import Any

import networkx as nx


def binary_search_movie_id(sorted_movies: list, movie_name: str) -> int:
    """Performs a binary search for a movie's id given the movie data and the movie name"""
    # Convert the dictionary to a list of tuples sorted by movie name
    # Initialize left and right pointers for binary search
    left, right = 0, len(sorted_movies) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_id, mid_name = sorted_movies[mid]

        if mid_name == movie_name:
            return mid_id
        elif mid_name < movie_name:
            left = mid + 1
        else:
            right = mid - 1

    # If the movie name is not found, return -1 (based on movies.csv we 100% know this will not be a valid id)
    return -1


def recommend_movies(user_names: list[str], user_ratings, movies_data: dict, G: nx.Graph()) -> list:
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
    # use a binary search function to get the ids of the users' inputted movies and accumulate them in a list
    user_movie_ids = []
    sorted_movies = sorted(movies_data.items(), key=lambda y: y[1])
    for x in user_names:
        user_id = binary_search_movie_id(sorted_movies, x)
        if user_id != -1:
            user_movie_ids.append(user_id)

    similarity_scores = {}
    for movie_id in user_movie_ids:
        for neighbour_id in G.neighbors(movie_id):  # networkx sadly does not have the canadian spelling :(
            if neighbour_id not in similarity_scores:
                similarity_scores[neighbour_id] = 0
            similarity_scores[neighbour_id] += G[movie_id][neighbour_id]['weight']

    sorted_recommendations = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)  # do I do quicksort here? idek

    recommended_movies = [(movie_id, movies_data[movie_id]) for movie_id, _ in sorted_recommendations if
                          movie_id not in user_movie_ids]

    return recommended_movies


def returned_movies(recommended_movies: list, genres: dict, actors: dict, movies_data: dict) -> Any:
    """Recursive function that lets the user pick ____"""
    # what is G doing here lol?
    # I think an overall problem is that the graphs seem highkey useless but idek, maybe try to figure out how to use
    # them later
    i = input("Input the movie you want to learn about: ")
    q = input("Which of the following would you like to know about the movie: ")
    sorted_movies = sorted(movies_data.items(), key=lambda y: y[1])
    movie_id = binary_search_movie_id(sorted_movies, i)  # binary search, list, id??. Perchance, what is faster RT? idek, can reverse dict if needed
    if q.upper() == "GENRE":
        # return genres[str(movie_id)]
        if str(movie_id) in genres:
            return genres[str(movie_id)]
        else:
            print(f'Type: {type(movie_id)}. {genres}')
            return
#     # elif inp.upper() == "RATING":
#     #     return ___
    elif q.upper() == "CAST":
        return actors[movie_id]
    else:
        print("Not a valid input, try again")
        returned_movies(recommended_movies, genres, actors, movies_data)  # there's something wrong here idk

    # if i in recommended_movies:
    #     inp = input("Which of the following would you like to know about the movie: ")
    #     if inp.upper() == "GENRE":
    #         return genres[i]
    #     # elif inp.upper() == "RATING":
    #     #     return ___
    #     elif inp.upper() == "CAST":
    #         return actors[i]
    #     else:
    #         print("Not a valid input, try again")
    #         returned_movies(recommended_movies, G, genres,
    #                         actors)  # how the fuck do I make it so i stays, add optional?
    # elif i.upper() == "EXIT":
    #     return
    # else:
    #     print("Not a valid input, try again")
    #     returned_movies(recommended_movies, G, genres, actors)

# figure out why this isn't working
