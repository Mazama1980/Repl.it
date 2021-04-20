"""Print the contents of the working directory:
Iterate over the contents of the working directory and:
1)skip over files or directories with names that begin with . or __
2)print the name of any directories followed by a /
3)print the name of everything else"""

from pathlib import Path

def workingdirectory():
    print("All files:")
    cwd = Path.cwd()

    for f in cwd.iterdir():
        print(f.name)


def directorynames():
    print("Directory name:")
    cwd = Path.cwd()

    for f in cwd.iterdir():
        if f.is_dir():
           print(f.name)


def contents():
    print("The word 'icecream' in '.py' files")
    cwd = Path.cwd()
    for f in cwd.iterdir():
        if f.suffix == ".py" and "icecream" in f.name:
            print(f.name)


def print_contents():
    """
        [x] skip over files or directories with names that begin with . or __
        [ ] print the name of any directories followed by a /
        [ ] print the name of everything else
    """
    print("print_contents()")
    cwd = Path.cwd()
    for f in cwd.iterdir():
        if f.name[0] != ".":
            print(f.name)

def skipdirectoryi():
    print("Skipped files that have underscores:")
    cwd = Path.cwd()
    for f in cwd.iterdir():
        if f.is_dir() == "_" in f.name:
            print(f.name)


"""List of files that end with .txt in the data file."""

def dottxtfiles():
    gt = Path("data")
    for h in gt.iterdir():
        if h.suffix == ".txt":
            print(h.name)



# workingdirectory()
# directorynames()
# contents()
#print_contents()
# skipdirectoryi()
dottxtfiles()