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
        [] use'fp.readlines()' to interate through each line in the file
        [] print each line for now
        
  """

def main():
      print("Hello World")
main()

from pathlib import Path
def load_csv():
    path = Path("data/flashcards/flashcards.csv").absolute()
    if not path.exists():
        print(f"This path {path} does not exist.")
        return
    if not path.is_file():
        print(f"Unable to read {path}.")
        return
    # fp = open("data/flashcards.csv")
    # fp.readlines()

load_csv() 