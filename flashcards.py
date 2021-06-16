"""
Flashcards
https://alissa-huskey.github.io/python-class/exercises/flashcards.html

[x] Part 1: Make a csv file
[x] Part 2: Start flashcards.py
[x] Part 3: start load_csv()
[x] Part 4: Read each line of the csv file
[x] Part 5: Get the card data from the csv file
[x] Part 6: Return the card data to main()
[x] Part 7: Remove extra whitespace
[x] Part 8: Skip the header row
[ ] Part 9: Start the play() function¶

    This function should take one argument, the list of cards. Eventually it
    will contain the user interface for running through each card, getting the
    answers from the user, and printing the score.

    For now we'll just write a play() function and call it.

    play()
    [x] write a play() function that takes one argument: cards
    [x] for temporary debugging, print something from it

    main()
    [x] call play() passing it the list of cards

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
        card["front"] = card["front"].strip()
        card["back"] = card["back"].strip()
        if card["front"] == "front" and card["back"] == "back":
            continue
        cards.append(card)
        print(card)
    fp.close()
    return(cards)


def play(cards):
    print("Hello from the Play Function")
    

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
    play(cards)
    

# ## Runner ##################################################################

# This calls the main() function if the script is being run directly
#   but not if it is being imported as a module

# This should always be at the very end of the script
#

if __name__ == "__main__":
    main()


