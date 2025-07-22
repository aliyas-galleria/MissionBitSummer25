import csv 

def load_movies(filename):

    movie_list = 'animation.csv'

with open('animation.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows('animation.csv')

with open('animation.csv', 'r') as file: 

   reader = csv.reader(file) 

   for row in reader: 
      print(row)

text = """Hello! Nice to meet you!"""

with open('example.txt', 'w') as file:
    file.write(text)

print("Text written to example.txt")

def load_movies(fileCsv):
    animation_list = []
    with open(fileCsv, 'r') as file: 

        reader = csv.reader(file) 

        next(reader)

        for row in reader: 

            animation_list.append(row)
    return animation_list


movie_list = load_movies('animation.csv')


def calculate_average_rating(movie_list):
    for movie in movie_list:
        ratings = int(movie_list[6])
    result = sum (ratings) / len(list)                
    print("The average rating of the following movies is", result)

calculate_average_rating('animation.csv')
    
