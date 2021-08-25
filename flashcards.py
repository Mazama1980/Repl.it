"""
Flashcards
# https://alissa-huskey.github.io/python-class/exercises/flashcards.html

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
[x] Part 15: Add topics menu
[x] Part 16: Allow answers with commas

    at the top of your file

      [x] import the csv module

    in load_csv() after opening your file

      [x] Create a new csv reader like so:

          reader = csv.reader(
          fh,
          quotechar="'",
          skipinitialspace=True,
          escapechar="\\"
          )
      [x] Instead of iterating over fh.readlines(), 
          iterate over the reader object, which will yields a list of values in each row.






"""
# ### Imports ################################################################
import random
from pathlib import Path
import textwrap
import time
import csv
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
    fp = open(path)
    reader = csv.reader(fp, quotechar="'", skipinitialspace=True, escapechar="\\")
    cards = list()
    for row in reader:
        if not row:
            continue
        card = dict()
        items = len(row)
        if items != 2:
            print("There is something wrong with this line. It doesn't equal 2 items.", path, row)
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
    print(0, "all")
    for i, path in enumerate(TOPICS, 1):
        #print the filename minus the .csv extension
        print(i, path.stem)
    selection = []
    choices = input("Choose one or more topics: ")
    for num in choices.split():
        if num == 0:
            return(TOPICS)
        num = int(num) - 1
        selection.append(TOPICS[num])
    print(selection)
    return(selection)    

# The main() function should be at the last function defined
#

def main():
    cards = []
    paths = menu()
    for path in paths:
        filecards = load_csv(path)
        if filecards:
           cards.extend(filecards)
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


