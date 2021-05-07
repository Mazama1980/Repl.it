"""Lessons/file-system-operations: lesson 13
   1. Create the data/tmp directory if it does not already exist.

   2. Use the touch() method to create files file_1.txt though file_9.txt."""

from pathlib import Path

def main():
    temp = Path("data/tmp")
    print(temp)
    filest = temp.joinpath("file_1.txt")
    filest.touch()
    temp.mkdir(exist_ok=True)

# main()

def multi_file():
    
    i = 1
    while i < 10:
        text = f"file_{i}.txt"
        print(i, f"{text}")
        i += 1

multi_file()
