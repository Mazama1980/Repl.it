films = [
    "Pinocchio",
    "Dumbo",
    "Bambi",
    "Alice in Wonderland",
    "Robin Hood",
]
for i, item in enumerate(films, 1):
    print(i, item)

# Ask the user what item the want to move

user = input("Type the number of your favorite movie.")

# Make sure it is a movie in the list

number_of_films = len(films)
if int(user) <= number_of_films:
    print(user)
else:
    print("That movie isn't there friends.")

# Move the movie to the new position

