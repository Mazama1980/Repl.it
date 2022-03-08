"""https://github.com/siporter43/mainpypet.py/blob/master/MovieList.py; https://github.com/siporter43/mainpypet.py/blob/master/MovieList.py
"""
films = [
    "Pinocchio",
    "Dumbo",
    "Bambi",
    "Alice in Wonderland",
    "Robin Hood",
]
for i, item in enumerate(films, 1):
    print(i, item)

# Ask the user what item they want to move

user = input("Type the number of your favorite movie.")

# Make sure it is a movie in the list

number_of_films = len(films)
if int(user) <= number_of_films:
    print(user)
else:
    print("That movie isn't there friends.")

# Move the movie to the new position
answer = int(user)
print(films[answer])

new_list = films[answer]


"""
Example of how it should work:

1 Pinocchio
2 Dumbo
3 Bambi
4 Alice in Wonderland
5 Robin Hood


Type the number of your favorite movie. 4

1 Alice in Wonderland
2 Pinocchio
3 Dumbo
4 Bambi
5 Robin Hood

"""

films = [
    "Pinocchio",
    "Dumbo",
    "Bambi",
    "Alice in Wonderland",
    "Robin Hood",
]
for i, item in enumerate(films, 1):
    print(i, item)

# [x] A. Ask the user what item the want to move

user = input("Type the number of your favorite movie.")

# [x] B. Make sure it is a movie in the list

number_of_films = len(films)
if int(user) <= number_of_films:
    print(user)
else:
    print("That movie isn't there friends.")

# [x] C. Print the name of the movie that they picked

answer = int(user) -1
print(f'You picked the movie {films[answer]}.')


# [x] D. Move the movie to the new position

films.insert(0, films[answer])
del films[int(user)]


# alternate, but worse, way
# # remove the selected film from the films list
# fav_film = films.pop(answer)

# # create an empty list with the favorite as the first
# fav_films = [fav_film]

# # go through the rest of the films and add them to the
# # to the fav_films list
# for film in films:
#     fav_films.append(film)


# [x] E. Print the list again in order with numbers next to each movie

for i, item in enumerate(films, 1):
    print(i, item)



def film_review():
    # list the movies
    for i, item in enumerate(films, 1):
        print(i, item)
    
    # ask the user
    # user = index number of movie (i) and the place number
    user = input("Type the number of your favorite movie.")
    number_of_films = len(films)
    
    # [x] B. Make sure it is a movie in the list
    if int(user) > 0 and int(user) <= number_of_films:
        print(user)
    else:
        print("That movie isn't there, friends. Try again")
        return
    answer = int(user) -1
    if answer < number_of_films:
        # [x] C. Print the name of the movie that they picked
        print(f'You picked the movie {films[answer]}.')
    
    place = input("What place in your favorites list would you like to put it?")
    # [x] D. Move the movie to the new position
    new_place = int(place)
    films.insert(new_place, films[answer])
    del films[int(user)]
    
    # [x] E. Print the list again in order with numbers next to each movie
    for i, item in enumerate(films, 1):
        print(i, item)



"""""""""We need to ask:
    What place would you like to move a movie in your favorites list? Input movie number, Place on user List
        ex. (4, 1) fourth movie in 1st spot... Needs to iterate through list...user input(Are you finished with list?)
        ex. if yes then print list, if no then Continue"""






