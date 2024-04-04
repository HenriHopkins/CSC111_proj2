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
    with open(movie_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for movie_id, name, _, _, _, _, _ in reader:  # change?
            titles[movie_id] = name
    genres = {}
    with open(genre_file, 'r', encoding='ascii') as file:  # change encoding??
        reader = csv.reader(file)
        next(reader)  # Skip header
        for movie_id, genre in reader:
            if movie_id not in genres.keys():
                genres[movie_id] = []
            genres[movie_id].append(genre)  # change with .setdefault?
    actors = {}
    with open(actor_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for movie_id, actor in reader:
            if movie_id not in actors.keys():
                actors[movie_id] = []
            actors[movie_id].append(actor)
    return (titles, genres, actors)  # change with .setdefault?


def read_csv_files_small(movie_file: str, genre_file: str, actor_file: str, k: int = 100) -> Tuple[
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
    with open(movie_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        c = 0
        for movie_id, name, _, _, _, _, _ in reader:  # change?
            if c <= k:
                titles[movie_id] = name
            c += 1
    genres = {}
    with open(genre_file, 'r', encoding='ascii') as file:  # change encoding??
        reader = csv.reader(file)
        next(reader)  # Skip header
        c = 0
        for movie_id, genre in reader:
            if c <= k:
                if movie_id not in genres.keys():
                    genres[movie_id] = []
                    c += 1
                genres[movie_id].append(genre)  # change with .setdefault?
    actors = {}
    with open(actor_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        c = 0
        for movie_id, actor in reader:
            if c <= k:
                if movie_id not in actors.keys():
                    actors[movie_id] = []
                    c += 1
                actors[movie_id].append(actor)
    return (titles, genres, actors)  # change with .setdefault?


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


def fast_one(movie_file: str, genre_file: str, actor_file: str) -> nx.Graph:
    """Reads the .csv files and constructs the graph concurrently"""
    G = nx.Graph()

    with open(movie_file, 'r', encoding='utf-8') as movie_file:
        movie_reader = csv.reader(movie_file)
        next(movie_reader)  # Skip header
        for movie_id, name, _, _, _, _, _ in movie_reader:
            G.add_node(movie_id, name=name)

    with open(genre_file, 'r', encoding='utf-8') as genre_file:
        genre_reader = csv.reader(genre_file)
        next(genre_reader)  # Skip header
        for movie_id, genre in genre_reader:
            if not G.has_node(movie_id):  # add movie_id if not present (delete?)
                G.add_node(movie_id)
            G.nodes[movie_id]['genres'] = G.nodes.get(movie_id, {}).get('genres', [])
            G.nodes[movie_id]['genres'].append(genre)

            # I question this lol pls fix

    with open(actor_file, 'r', encoding='utf-8') as actor_file:
        actor_reader = csv.reader(actor_file)
        next(actor_reader)  # Skip header
        for movie_id, actor in actor_reader:
            if not G.has_node(movie_id):
                G.add_node(movie_id)
            G.nodes[movie_id]['actors'] = G.nodes.get(movie_id, {}).get('actors', [])
            G.nodes[movie_id]['actors'].append(actor)

    # Construct edges based on common genres and actors
    for movie_id, movie_data in G.nodes(data=True):
        for other_movie_id, other_movie_data in G.nodes(data=True):
            if movie_id != other_movie_id:
                common_genres = set(movie_data.get('genres', [])) & set(other_movie_data.get('genres', []))
                common_actors = set(movie_data.get('actors', [])) & set(other_movie_data.get('actors', []))
                if common_genres:
                    G.add_edge(movie_id, other_movie_id, weight=len(common_genres) * 5)
                if common_actors:
                    G.add_edge(movie_id, other_movie_id, weight=len(common_actors) * 2)

    return G
