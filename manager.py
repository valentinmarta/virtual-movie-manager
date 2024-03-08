from movie import Movie

class Manager:
    def __init__(self):
        self.movie_list : list[Movie] = []

    def create_movie(self):

        name = input("Type the name of the movie: ").lower().capitalize()

        # checking if the movie exists
        for movie in self.movie_list:
            if name == movie.name:
                print("This movie already exists on the list, please try again with another movie")
                return
            
        while True:
            try:
                year = int(input("Type the year of the movie: "))
                break
            except Exception as e:
                print(f"Error: {e}")
        gender = input("Type the gender of the movie: ").lower()
        country = input("Type the country of the movie: ").capitalize()
        score = input("Type the score of the movie: ")

        movie = Movie(name, year, gender, country, score)
        self.movie_list.append(movie)

    def verify_movie(self):

        if not self.movie_list:
            print("The list is empty")
            return
        
        movie_name = input("Type the name of the movie: ").lower().capitalize()

        for movie in self.movie_list:
            
            if movie_name == movie.name:
                print("The movie is on the list")
                return
            
        print("The movie is not on the list")

    def year(self):
        
        flag = True

        if not self.movie_list:
            print("The list is empty")
            return
        
        while True:
            try:
                year = int(input("Type the year of the movie you are looking for: "))
                break
            except Exception as e:
                print(f"Error: {e}")

        for movie in self.movie_list:
            
            if year == movie.year:
                print(movie.name)
                flag = False

        if flag:
            print("we dont have any movie that match with that year")

        return
    
    def present_movie(self):

        if not self.movie_list:
            print("The list is empty")
            return
        
        movie_name = input("Type the name of the movie you want to present: ").lower().capitalize()

        for movie in self.movie_list:

            if movie_name == movie.name:
                movie.present()
                return
            
        print("We dont have any movie with that name")

    def ch_gender(self):

        if not self.movie_list:
            print("The list is empty")
            return
        
        movie_name = input("Type the name of the movie: ").lower().capitalize()

        for movie in self.movie_list:

            if movie_name == movie.name:
                
                new_gender = input("Type the new gender of the movie: ")
                movie.change_gender(new_gender)
                return
            
        print("We dont have any movie with that name.")