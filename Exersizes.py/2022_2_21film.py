"""  https://github.com/siporter43/mainpypet.py/blob/master/MovieList.py
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

# move the part of the film_review() function that actually changes the films list
# to a new function called move_film(). It should take two arguments:
# - film_id (what the user types in to the first question)
# - new_position (what the user types in to the second question)



# [x] A. Ask the user what item the want to move

def move_film(film_id, new_position):
    # [x] D. Move the movie to the new position
    new_place = int(new_position) - 1
    films.insert(new_place, f"+ {films[film_id]}")
    # films.insert(new_place, films[answer])
    del films[film_id]
        
def film_review():
    # list the movies
    for i, item in enumerate(films, 1):
        print(i, item)
    
    # ask the user
    # user = index number of movie (i) and the place number
    user = input("Type the number of your favorite movie. ")
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
    
    place = input("What place in your favorites list would you like to put it? ")
    # [x] D. Move the movie to the new position
    move_film(answer, place)
    
    # [x] E. Print the list again in order with numbers next to each movie
    for i, item in enumerate(films, 1):
        print(i, item)


"""""""""We need to ask:
    What place would you like to move a movie in your favorites list? Input movie number, Place on user List
        ex. (4, 1) fourth movie in 1st spot... Needs to iterate through list...user input(Are you finished with list?)
        ex. if yes then print list, if no then Continue"""



# alternate, but worse, way
# # remove the selected film from the films list
# fav_film = films.pop(answer)

# # go through the rest of the films and add them to the
# # to the fav_films list
# for film in films:
#     fav_films.append(film)

# Runner

FILMS = films.copy()

def test_move_film_0_3():
    films = FILMS.copy()
    move_film(0, 3)

    wanted = ["Dumbo", "Bambi", "Alice in Wonderland", "+ Pinocchio", "Robin Hood"]

    assert films == wanted, \
        f"After moving 0 to 3 the film order should be: \n{wanted} but instead it's: \n{films}"

def test_move_film_3_0():
    films = FILMS.copy()
    assert films == FILMS, "copy failure"

    move_film(3, 0)

    wanted = ["+ Alice in Wonderland", "Pinocchio", "Dumbo", "Bambi", "Robin Hood"]

    assert films == wanted, \
        f"After moving 3 to 0 the film order should be: \n{wanted} but instead it's: \n{films}"

# test_move_film_0_3()
# test_move_film_3_0()

def silly_test():
    films = FILMS.copy()
    assert films[0] == "Pinocchio", "Not correct"

# film_review()
silly_test()

