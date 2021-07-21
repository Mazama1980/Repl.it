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
[x] Part 9: Start the play() function
[x] Part 10: Go through each card in random order
[x] Part 11: Test the user
[x] Part 12: Scorekeeping
[x] Part 13: Prettify flashcards

    throughout your file:

        [x] get rid of any debug print() statements

    at the top of your file:

        [x] make a global variable WIDTH and set it to around 75

    in play():

        [x] print a line to the beginning and end of each card

        [x] add some extra newlines around various elements

        [x] center any string by calling the .center() method on it and pass the
            argument WIDTH. For example, the card["front"] line.

        [x] right align any string by calling the .rjust() method on it and
            passing the argument WIDTH. For example, the card x of y line.

        [x] print "score of total" after the end of each card
  
"""
# ### Imports ################################################################
import random
from pathlib import Path
import textwrap
import time

# ## Global Variables ########################################################
WIDTH = 60
MARGIN = 20
MAXWIDTH = WIDTH - MARGIN
DEBUG_MODE = True

# ## Functions ###############################################################

def load_csv(path):
    if not path.exists():
        print(f"This path {path} does not exist.")
        return
    if not path.is_file():
        print(f"Unable to read {path}.")
        return
    # print(f"Loading file: {path}.")
    fp = open("data/flashcards/flashcards.csv")
    cards = list()
    for line in fp.readlines():
        if line == '\n':
            continue
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
    fp.close()
    return(cards)


def play(cards):
    total = len(cards)
    num = 1
    score = 0
    while cards:
        print("*" * WIDTH)
        box = "|"
        print(box.ljust(WIDTH-59), box.rjust(WIDTH-2))
        tallytext = f"card {num} of {total}"
        print("|" + tallytext.rjust(WIDTH-2) + "|")
        print(box.ljust(WIDTH-59), box.rjust(WIDTH-2))
        card = random.choice(cards)
        cards.remove(card)
        head = "Question:"
        print("|" + head.center(WIDTH-2) + "|")
        query = textwrap.wrap(card["front"], MAXWIDTH)
        for line in query:
            print("|" + line.center(WIDTH-2) + "|")
            print(box.ljust(WIDTH-59), box.rjust(WIDTH-2))
        if DEBUG_MODE:
            i = 5
            while i > 0:
                print("| " "Cheat-- the answer is:", card["back"])
                print(box.ljust(WIDTH-59), box.rjust(WIDTH-2))
                # print(".", end="")
                time.sleep(1)
                i = i - 5
        answer = input("| " + "Your answer: ")
        if answer == card["back"]:
            score = score + 1
            print("*" * WIDTH)
            print("Correct! Your score is: ", score)
        else:
            print("INCORRECT", card["back"])
            print("-" * WIDTH)
        reply = input("Would you like to continue? ")
        if reply == "n":
            break
        num = num + 1
    print("score of ", score)
        

    

# The main() function should be at the last function defined
#

def main():
    path = Path("data/flashcards/flashcards.csv")
    cards = load_csv(path)
    if not cards:
        print("This file is empty.")
        return
    play(cards)
    

# ## Runner ##################################################################

# This calls the main() function if the script is being run directly
#   but not if it is being imported as a module

# This should always be at the very end of the script
#

if __name__ == "__main__":
    main()


