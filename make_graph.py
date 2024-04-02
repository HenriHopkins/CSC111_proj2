import csv
from typing import Tuple
import networkx as nx


def read_csv_files(movie_file: str, genre_file: str, actor_file: str) -> Tuple[
    dict, dict, dict]:  # figure out type annotation
    """Reads the .csv files that have relevant data for the project. Returns a tuple of lists (one  for each file)"""
    # movies = dict()
    # with open(movie_file, 'r') as file:  # figure out wtf is wrong with the str by looking at ex3 later
    #     reader = csv.reader(file)
    #     next(reader)
    #     for movie_id, name, _, _, _, _, _ in reader:
    #         movies[movie_id] = name
    # how do I build the graph, idek
    titles = {}
    with open(movie_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for movie_id, name, _, _, _, _, _ in reader:
            titles[movie_id] = name
    genres = {}
    with open(genre_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for movie_id, genre in reader:
            movies[movie_id] = name  # where am I putting genre list? I have no idea lol.

    return (movies,)


def construct_graph(movies_data, genres_data, actors_data) -> nx.Graph():
    """Returns a weighted graph constructed with the relevant data"""
    #  I could do this with file reader for max efficiency perchance but idk if it's the move, is there
    #  any value in having them as lists if I already have them in self._vertices
    G = nx.Graph()
    # Add nodes
    for movie_id in movies_data:
        G.add_node(movie_id)

    # Add edges based on genres
    for movie_id, genres in genres_data.items():
        for other_movie_id, other_genres in genres_data.items():
            if movie_id != other_movie_id:
                common_genres = set(genres) & set(other_genres)
                if common_genres:
                    G.add_edge(movie_id, other_movie_id, weight=5)

    # Add edges based on actors
    for movie_id, actors in actors_data.items():
        for other_movie_id, other_actors in actors_data.items():
            if movie_id != other_movie_id:
                common_actors = set(actors) & set(other_actors)
                if common_actors:
                    G.add_edge(movie_id, other_movie_id, weight=2)
    return G

def build_graph()
