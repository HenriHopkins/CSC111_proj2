import csv
if __name__ == "__main__":
    movies = dict()
    with open("files/movies.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for movie_id, name, _, _, _, _, _ in reader:
            movies[movie_id] = name
