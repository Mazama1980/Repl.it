"""Moving and renaming files."""

"""Exercise 15 (Rename file)

    []Rename the file_1.txt that you created earlier to file_01.txt.

    []Be sure to check first that the target does not already exist.

    []Print the files new name.."""

from pathlib import Path


def main():
    path = Path("data/tmp/file_1.txt")
    if path.exists():
        print(path)
    else:
        print("no such file")

# main()

def rename():
    old_name = Path("data/tmp/file_1.txt")

    if not old_name.exists():
        print(f"Sorry, this file {old_name} does not exist.")
        return
    new_name = Path("data/tmp") / "file_01.txt"

    if new_name.exists():
        print("Sorry, this file already exists")
    else:
        old_name.replace(new_name)
        print(f"file moved to: {new_name}")

rename()