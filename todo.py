"""File I/O. Reading Files Lesson 3/1/2021"""

def todo():
   print("ToDo")
   print("======")


   fh = open("todo.txt")
   for line in fh.readlines():
    
       print("* " + line, end="")
   fh.close()


def todos():
    todos = [
        "laundry",
        "dishes",
    ]
    fh = open("todo.txt", "w")
    for item in todos:
        fh.write(f" - {item}\n")
    fh.close()


def groceries():
    groceries = [
        "beets",
        "mayo",
        "tortillas",
        "cereal",
    ]
    fh = open("groceries.txt", "w")
    for item in groceries:
        fh.write(f" - {item}\n")
    fh.close()

# height = 72

# fh.write(" - " + item + "\n")

# print("My height: " + height)
# print("My height:", height)
# print(f"My height: {height}")


def append_todos():
    fh = open("todo.txt", "a")
    fh.write("- dust\n")
    fh.close


def append_groceries():
    fh = open("groceries.txt", "a")
    fh.write(" - milk\n")
    fh.close()


def with_groceries():
    with open("groceries.txt") as fp:
        contents = fp.read()

    print("groceries")
    print("=========")
    print(contents)


def print_brownie():
    fh = open("mug-brownie.md")
    contents = fh.read()
    fh.close()

    print(contents)


def mug_brownies():
    with open("mug-brownie.md") as fp:
        contents = fp.read()

    print(contents)



# todo()
# todos()
# groceries()
# append_todos()
# append_groceries()
# with_groceries()
# mug_brownies()