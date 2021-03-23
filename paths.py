
from pathlib import Path

def main():
    path = Path("data/contacts.txt")
    if not path.exists():
        print("Sorry, no file named contacts.txt")
        return

    if not path.is_file():
        print("Unable to read file contacts.txt")
        return

    fh = open(path)
    contents = fh.read()
    fh.close()
    print(contents)

def groceries():
    food = Path(__file__).parent / "data" / "groceries.txt"
    
    fh = open(food)
    with open(food):
        contents = fh.read()
        print(contents)

main()
groceries()