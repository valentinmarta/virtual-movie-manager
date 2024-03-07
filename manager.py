from movie import Movie

class Manager:
    def __init__(self):
        self.movie_list : list[Movie] = []

    def create_movie(self):

        name = input("Type the name of the movie").lower().capitalize()

        # checking if the movie exists
        for movie in self.movie_list:
            if name == movie.name:
                print("This movie already exists on the list, please try again with another movie")
                return
            
        year = input("Type the year of the movie")
        gender = input("Type the gender of the movie").lower()
        country = input("Type the country of the movie").capitalize()
        score = input("Type the score of the movie")

        movie = Movie(name, year, gender, country, score)
        self.movie_list.append(movie)
