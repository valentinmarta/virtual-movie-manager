class Movie:

    def __init__(self, name, year, gender, country, score):

        self.name = name
        self.year = year
        self.gender = gender
        self.country = country
        self.score = score

    def present(self):
        print(f"Movie name: {self.name}, Year: {self.year}, Gender: {self.gender} Country: {self.country}, Score: {self.score}")

    def change_gender(self, new_gender):
        self.gender = new_gender

    def change_score(self, new_score):
        if new_score <= 10 and new_score >= 1:
            self.score = new_score
        else:
            print("invalid value, try again with a number between 1 and 10")