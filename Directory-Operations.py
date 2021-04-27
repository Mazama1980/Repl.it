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

def listcontents():
    path = Path("contacts.txt")
    path = path.absolute()
    print(path)
    path.touch()

# listcontents()


def datacontents():
    """Touch contacts.txt in the data directory."""
    cwd = Path.cwd()
    basedir = cwd.joinpath("data")
    path = basedir.joinpath("flowers.txt")
    print("datacontents():", path)
    path.touch()

# datacontents()

def data_tmp():
    """1. If it does not already exist, create the data/tmp directory
       2. Create the empty file file_1.txt using the touch() method. """
    path = Path("data/tmp")
    path.mkdir(exist_ok=True)
    filepath = path.joinpath("file_1.txt")
    filepath.touch()

    print("data_tmp:", filepath)

data_tmp()

def delete():
    """1. Choose one of your generated files to delete.

       2. Ask the user to confirm they want to delete the file.

       3. Use unlink() to delete the file."""
    path = Path("data/tmp/file_1.txt")
    print("Are you sure you want to throw good code away?")
    if input() != "y":
        print("Sorry to hear that.")
    else:
        path.unlink(missing_ok=True)   

    
delete()