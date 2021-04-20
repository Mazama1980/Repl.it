"""# Three ways to make a path to a tmp directory inside a data directory:

# 1. use the full path as an argument when you create the Path object
path = Path("data/tmp")

# 2. use joinpath
path = Path("data").joinpath("tmp")

# 3. use the / operator
path = Path("data") / "tmp."""

"""Exercise 11 (Create a directory)

Create a tmp directory in your data directory. If you don’t have a data directory, create it first."""

from pathlib import Path

def removetmp():
    path = Path("data/tmp")
    print("Removing directory", path)
    path.rmdir()


def addtmp():
    path = Path("data/tmp")
    print("Adding directory", path)
    path.mkdir(exist_ok=True)
    

# addtmp()
# removetmp()


def touchtmp():
    """Creating empty files using touch()."""
    path = Path("tmp.py")
    path.touch()



# touchtmp()


