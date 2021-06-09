"""
Flashcards
https://alissa-huskey.github.io/python-class/exercises/flashcards.html

[x] Part 1: Make a csv file
[x] Part 2: Start flashcards.py
[x] Part 3: start load_csv()
[x] Part 4: Read each line of the csv file
[x] Part 5: Get the card data from the csv file
[ ] Part 6: Return the card data to main()
[ ] Part 7: Remove extra whitespace

    The load_csv() function should take one argument, a Path object to a csv
    file. Eventually it will return a list where each item is a dict with
    "front" and "back" keys, one for each row in the file except the header.

    For now though, make a simple function that just takes a Path object, prints
    the location, and makes sure the file exists.

    load_csv()

        [x] write a load_csv() function that takes one argument: path
        [x] check to make sure the csv file exists. If not, print an error
            message that includes the path then return
        [x] print a temporary debug message: "loading file: path"

    in main()

        [x] make a Path object to your csv file
        [x] call your load_csv() function, passing it your Path object as the
            argument
        [x] and assign the returned value to a variable named cards

    in load_csv()

        [x] open the csv file in read mode using the open() function
        [x] use fp.readlines() to iterate through each line in the file
        [x] for temporary debugging, print each line

    in load_csv(), in the readlines() loop

        [x] make an empty dict assigned to a variable named card
        [x] split each line on the "," using the .split() method and assign the
            result to a variable named row
        [x] check that there are two items in the row using the len() function.
            If not print an error message and return
        [x] assign card["front"] to the first item in the row, and card["back"]
            to the second
        [x] for temporary debugging, print the card dict


    Have load_csv() put all of the card dictionaries into one big cards list and return that to main().

    in load_csv(), before the readlines() loop

        [x] make an empty list assigned to a variable named cards
            in load_csv(), at the end of the readlines() loop
        [x] use the .append() method on the cards list with the argument card
            in load_csv(), after the loop
        [x] return cards

        in main()

        [ ] if the cards list is falsy, return
        [ ] otherwise, print the cards list for temporary debugging

        

    In order to make sure that the flashcards are printed nicely and that the
    users answers get matched up correctly, the trailing "\n" needs to be
    removed from the end of each line. Any extra spaces that happen to be around
    the "," or at the beginning or end of the line also need to be removed.

    in load_csv(), in the loop

        [ ] remove leading and trailing whitespace by calling the .strip()
            method on card["front"] and card["back"]
  """
# ### Imports ################################################################

from pathlib import Path

# ## Global Variables ########################################################

# ## Functions ###############################################################

def load_csv(path):
    if not path.exists():
        print(f"This path {path} does not exist.")
        return
    if not path.is_file():
        print(f"Unable to read {path}.")
        return
    print(f"Loading file: {path}.")
    fp = open("data/flashcards/flashcards.csv")
    cards = list()
    for line in fp.readlines():
        card = dict()
        row = line.split(",")
        items = len(row)
        if items != 2:
            print("There is something wrong with this line. It doesn't equal 2 items.")
            return
        card["front"] = row[0] 
        card["back"] = row[1]
        cards.append(card)
        print(card)
    fp.close()
    return(cards)



# The main() function should be at the last function defined
#

def main():
    print("Hello World")
    path = Path("data/flashcards/flashcards.csv")
    cards = load_csv(path)
    if not cards:
        print("This file is empty.")
        return
    else:
        print(cards)
    

# ## Runner ##################################################################

# This calls the main() function if the script is being run directly
#   but not if it is being imported as a module

# This should always be at the very end of the script
#

if __name__ == "__main__":
    main()


