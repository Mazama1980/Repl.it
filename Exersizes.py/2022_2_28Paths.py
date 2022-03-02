"""2022-2-28 Path Exercise 2.10 (Ex.66)"""


from pathlib import Path

def main():
    path = Path.home() / "todo.txt" / "groceries.txt"

    with open(path) as fh:
        contents = fh.read()

    print

from pathlib import Path


def main():

    path = Path(__file__).absolute()
    print("The file you are running is:", path)

    my_dir = path.parent
    print("The directory that the file is in is:", my_dir)

    my_path = my_dir.joinpath("data").joinpath("file.txt")
    my_path = my_dir / "data" / "file.txt"
    
    print("The path to your file is:", my_path)
    
    path = Path("/home/runner/PythonClass/data/file.txt")
    print("your path is:", path)
    
    if not path.exists():
        print("No such file")
    
    if not path.is_file():
        print("Silly goose, this is not a file.")
    
    if not path.is_dir():
        print("Yeah, no, wrong not a directory.")

    path = path.absolute()
    print("now your path is:", path)
    
main()

