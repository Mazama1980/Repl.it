"""Exercise 15 (Move file)

[x]Use .touch() to make an empty file xxx.txt

[x]Make a new Path object to data/xxx.txt

[x]Check to make sure data/xxx.txt does not exist, and print an error if it does.

[x]Print a message "Moving ‘{from}’ to ‘{to}’."

[x]Use .replace() to move the file."""

from pathlib import Path

def move_file():
    new_file = Path("xxx.txt")
    print(f"The new file is {new_file}")
    new_file.touch()
    newest_file = "data" / new_file
    if newest_file.exists():
        print(f"Warning! This file '{newest_file}' already exists.")
    else:
        newest_file = new_file.replace("data/xxx.txt")
        print(f"File moved from '{new_file}' to '{newest_file}'.")


move_file()

"""Exercise 17 (Rename file)

[]Rename the file_1.txt that you created earlier to file_01.txt.

[]Be sure to check first that the destination does not already exist.

[]Print the files new name."""

def rename_file():
    route = Path("data")
    old_wire = route / "file_1.txt"
    new_wire = route / "file_01.txt"

    if new_wire.exists:
        print(f"This file {new_wire} already exists.")
    else:
            old_wire.replace("new_wire")

# rename_file()