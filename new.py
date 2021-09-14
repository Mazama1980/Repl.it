# general syntax notes
# the types of syntax associated with values
#
# dot notation: access the attributes of an object
#   a dot followed by the attribute
# value.name

# calls: executes a function, method or type
#   use parenthesis
# value()

# subscription: access the elements of a collection
#   square brackets
# value[expression]
#
# using parenthesis for grouping and order of operation
# num = (5+5)* 3
# string = ("the number is: " + str(num)).center(30)

# review of lists
# animals = ["garfield", "mr. ed", "mr. Limpit"]
# print(animals[0])


# TODO
# [x] reorganize your file to use a main() function
#     [x] make PETS a global variable
#     [x] put everything after defining PETS into a main() function
#     [x] call main()

# [x] use a variable to access a pet species
#     [x] assign the variable name to a string that is the same as one of
#         the keys in your PETS dictionary
#     [x] print "NAME is a SPECIES", but replace
#         * [x] NAME with the name variable, and
#         * [x] SPECIES with the value from the PETS dictionary associated with the name key

# [x] print the species a user asks for
#     [x] change the value of the name variable from a string to input from the user
#         note: it should still print out "NAME is a SPECIES", but now it will
#         change depending what the user types

#GLOBAL
PETS = {
    "garfield": "cat",
    "mr. ed": "horse",
    "mr. limpit": "fish",
}

def main():
    # add a key value pair to the PETS dictionary
    PETS["stitch"] = "alien"

    # change the value associated with a key
    PETS["mr. limpit"] = "Fish"
    
    # remove a key value pair from the dictionary
    del PETS["mr. limpit"]

    # using a variable as the key
    name = input("What name? ")
    # print("NAME is a SPECIES")
    print(name, "is an", PETS[name])

    # check if a dictionary has a key
    if "garfield" in PETS:
        print("yep, garfield is in PETS")

    # print the whole dictionary
    print("PETS:", PETS)

    # print a value associated with a key
    print("garfield is a:", PETS["garfield"])

    # get a list of keys
    print("PETS keys:", PETS.keys())

    # get a lit of values
    print("PETS values:", PETS.values())

    if "horse" in PETS.values():
        print("yes, horse is a value in the PETS dictionary")

main()