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
[x] Part 14: Wrap long questions¶
[ ] Part 15: Add topics menu
    
    at the top of your file

      [x] Make a list assigned to the global variable TOPICS

    menu()

      [ ] write a menu() function

      [ ] assign TOPICS to a list of Path objects in your flashcards directory
          using the .iterdir() method

      [ ] print an error message if no files are found in your flashcards
          directory

      [ ] print the filename minus the .csv extension for each Path object in
          the TOPICS list, next to a number

      [ ] print a special option "all" with a menu selection of 0

      [ ] make a list assigned to the variable selection

      [ ] get input from the user asking them to choose one or more topics and
          assign it to a variable choices

      [ ] use the .split() method to split choices into multiple items on
          whitespace

      [ ] iterate over each response and assign to num:

          [ ] if the response is "0", return TOPICS

          [ ] convert num to an int and subtract 1

          [ ] get the item from TOPICS at the num index and append it to
              selection list

          [ ] return the selection list

    in main()

        [ ] at the beginning of the function, make an empty cards list

        [ ] call menu() and assign the returned value to the variable paths

        [ ] remove the line where you previously defined the path to your .csv
            file

        [ ] iterate over paths and assign each element to the variable path:

        [ ] call load_csv() with the path argument

        [ ] append the returned value to cards using the .extend() method


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
TOPICS = []
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
                print("| ", "Cheat-- the answer is:", card["back"])
                print(box.ljust(WIDTH-59), box.rjust(WIDTH-2))
                # print(".", end="")
                time.sleep(1)
                i = i - 5
        answer = input("| Your answer: ")
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
        

def menu():
    datadir = Path("data/flashcards")
    # breakpoint()
    if not datadir.is_dir():
        print(f"This path {datadir} does not exist.")
    TOPICS = list(datadir.iterdir())
    # datadir is: a Path object
    # datadir.iterdir(): generator object that lists files in the directory
    print(TOPICS)    

    
    

# The main() function should be at the last function defined
#

def main():
    menu()
    return
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


