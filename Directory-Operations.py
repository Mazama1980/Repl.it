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

# data_tmp()

def delete():
    """1. Choose one of your generated files to delete.

       2. Ask the user to confirm they want to delete the file.

       3. Use unlink() to delete the file."""
    path = Path("data/tmp/file_1.txt")
    print("Are you sure you want to throw good code away?")
    if input() != "y":
        print("Okay. It's deleted.")
    else:
        path.unlink(missing_ok=True)   

    
# delete()

def presents():
    """
    People files

    This exercise is to generate files for a list of people that you can use to
    keep track of notes, birthday info, gift ideas etc.

    At the end of the exercise you should have a folder containing a file for each
    person that contains something related to that person.

    [x] Make a list of people's names that you'd like to keep track of information about.
    [x] Create a new directory called something like `people` if it does not exist.
    [x] Iterate over the list of people.
        [x] Create a blank file called `{name}.txt` in the `people` directory if it doesn't exist.
        [x] Write something to the file about that person

    [x] Write something different for each person in the list
        [x] Change the list to a dict where the key is the name of the person
            and the value is a gift idea.
        [x] Change your for loop to get the name and gift of each item
            in the dict using the .items() method
        [x] Write a second line to the file with their gift idea

    """
    
    print("Hello")
    people = {
        "Grumpy": "massager", 
        "Doc": "hemp oil", 
        "Sleepy": "Redbull", 
        "Dopey": "reminder diary", 
        "Bashful": "flowers ", 
        "Happy": "chocolates"
    }

    # number = 42
    # number, meaning = 42, "life, the universe, everything"

    # # these three lines are all handled automaticaly by the for loop
    # # you don't need an i
    # i = 0
    # people_items = people.items()
    # while i < len(people_items):
    #     # this assignment line is the key part of the for loop
    #     # here, `name, gift` is the x in `for x in y`
    #     name, gift = people_items[i]
    #     # the rest of the for loop
        # ...

    folder = Path("data") / "Presents"
    folder.mkdir(exist_ok=True)
    for name, gift in people.items():
        filename = f"{name}.txt"
        filepath = folder / filename
        print(f"file for {name} is: {filepath}")
        filehandler = open(filepath, "w")
        filehandler.write(f"Presents for {name}\n\n")
        filehandler.write(f"* {gift}\n")
        filehandler.close()
        filepath.touch(exist_ok=True)
        
       
    


presents()