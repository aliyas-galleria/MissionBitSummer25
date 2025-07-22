movies = [
    ["Action", "Die Hard", "8.2"],
    ["Romance", "The Notebook", "7.8"],
    ["Adventure", "Lord of the Rings", "8.9"],
    ["Comedy", "Dumb and Dumber", "7.3"],
    ["Horror", "Scream", "7.4"],
    ["Science Fiction", "Star Wars", "8.6"]
]

ratings = [float(movie[2]) for movie in movies]

num = ratings [5]
if num >= 8:
    print("Great movie!👍")
elif num > 5 and num < 7.9:
    print("Okay movie.👌")
else:
    print("Not worth watching.👎")

movie_names = [movie[1] for movie in movies]
for movie in movie_names:
    print("There are many movies but", movie, "is a great one!")

total_sum = sum(ratings)
print("The total of all the movie ratings in the list is:",total_sum)

for i, movie in enumerate(movie_names):
    print(f"Movies in this list include: {movie_names[i]}.")

for i, movie in enumerate(movie_names):
    print(f"{movie_names[i]} has a rating of {ratings[i]}.")

max_value = max(ratings)
print(f"The movie with the highest rating in this list has an {max_value}.")

target_genre = "Action"
filtered_movies = []

for movie in movies:
    if movie[0] == target_genre:
        filtered_movies.append(movie)
print(filtered_movies)

def calculate_average_rating(ratings):
    result = int(total_sum) / len(ratings)                    
    print("The average rating of the following movies is", result)

calculate_average_rating(ratings)

def find_highest_rated(movies):
    max_value = max(ratings)
    highest_movie = ""
    highest_movie = (movie[1])
    print(f"The highest rated movie is {highest_movie} with a rating of {max_value}.")

find_highest_rated(movies) 