import csv
if __name__ == "__main__":
    movies = dict()
    with open("files/movies.csv", 'rb') as file:
        reader = csv.reader(line.decode('utf-8') for line in file)
        next(reader)
        for movie_id, name, _, _, _, _, _ in reader:
            movies[movie_id] = name
    for x in movies.items():
        print(x)
