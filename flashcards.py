"""Flashcards

    Setup
    -----
    1. Create a folder data/flashcards if it doesn't exist
    2.Make flashcard csv files
        [] In the data/flashcards directory manually make file called ending in .csv
        [] Each line shoud be one card with the format: "text for front, text for back".
        Here is my "path.csv" example:
        
        import the Path class, from pathlib import Path
        check if Path object path exists, path.exists()
        check if Path object path is a file, path.is_file()
        check if Path object path is a directory, path.is_dir()

    Exercise
    -------
    1. Start your flashcards.py file
        [x] write a main () function, and in it print something, then call it
    2. Write a load_csv function
        [] open the csv file you made using the 'open()' function
        [] use'fp.readlines()' to iterate through each line in the file
        [] print each line for now
        
  """
# ### Imports ################################################################

from pathlib import Path

# ## Global Variables ########################################################


# ## Functions ###############################################################

def load_csv():
    print("hello")
    path = Path("data/flashcards/flashcards.csv")
    if not path.exists():
        print(f"This path {path} does not exist.")
        return
    if not path.is_file():
        print(f"Unable to read {path}.")
        return
    # fp = open("data/flashcards.csv")
    # fp.readlines()


# The main() function should be at the last function defined
#

def main():
    print("Hello World")
    load_csv() 

# ## Runner ##################################################################

# This calls the main() function if the script is being run directly
#   but not if it is being imported as a module

# This should always be at the very end of the script
#

if __name__ == "__main__":
    main()


