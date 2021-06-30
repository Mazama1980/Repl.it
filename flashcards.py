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

   in play(), in the loop

    [x] print card["front"]

    [x] prompt the user for their answer using the input() function and assign the result to a variable named answer

    [x] check if the answer is the same as card["back"]
        * [x] if so, increment score by one and print "CORRECT"
        * [x] if not, print "INCORRECT", then cards["back"]

    [x] call input() asking if the user wants to continue

    in play(), after the loop
"""
# ### Imports ################################################################
import random
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
    # print(f"Loading file: {path}.")
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
    fp.close()
    return(cards)


def play(cards):
    score = 0
    while cards:
        card = random.choice(cards)
        cards.remove(card)
        print(card["front"])
        print("Cheat-- the answer is:", card["back"])
        answer = input("Your answer: ")
        if answer == card["back"]:
            score = score + 1
            print("Correct! Your score is: ", score)
        else:
            print("INCORRECT", card["back"])
        reply = input("Would you like to continue? ")
        if reply == "n":
            break
        

        # print("Hi", card)

    

# The main() function should be at the last function defined
#

def main():
    print("Hello World")
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


