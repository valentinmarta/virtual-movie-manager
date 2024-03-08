from manager import Manager

def main():

    object = Manager()

    while True:

        # Options for the user
        op = input("""Welcolme to our virtual movie manager, please select one option:
        1. Create movie.
        2. Verify if the movie is already on the list.
        3. Ask for all the movies of one specific year.
        4. Present one movie of the list.
        5. Change the type of the movie.
        6. Exit.
        """)

        # Menu with functions
        if op == "1":
            object.create_movie()
        elif op == "2":
            object.verify_movie()
        elif op == "3":
            object.year()
        elif op == "4":
            object.present_movie()
        elif op == "5":
            object.ch_gender()
        elif op == "6":
            print("Thank you for using ous service")
            break
        else:
            print("invalid value, try again")

if __name__ == "__main__":
    main()