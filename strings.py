"""Exercise 56 (String Creation)

    1. Use a docstring to split the lymric or lullaby of your choice into a multi-line string and assign it to the variable verse, then print it.

    2. Using one double-string or single-quoted string, print the words "one", "two", and "three" on three seperate lines.

    3. Print a double quoted string that includes double quotes. Print a single quoted string that includes single quotes.

    4. Print a string that includes backslashes by escaping the backslash. Print a second string that includes backslashes using an r-string.
"""

def somefunc():
    """This is a pointless function that does nothing.
    Except for demonstrate docstrings.
    On newlines!
    """
    ...

# print(somefunc.__doc__)
# help(somefunc)

verse = """There was an Old Man with a beard,
Who said, 'It is just as I feared!
Two Owls and a Hen, Four Larks and a Wren,
Have all built their nests in my beard!'"""
print(verse)

numb = "one\ntwo\nthree"
print(numb)

print("We are \"up\" in the air!")

print('We\'re \'up\' in the air?')

print("Hack\\whack are two other words for backslash.")

print(r"my birthday is 7\12\1961")

print("The two previous print statements are using the backslash symbol \'\\' incorrectly.")

some_stuff = [
    1,
    2,
    3,
    4,
]

print("x"*(3 + 2))

text = """
        Light streams in through the window against the
        north wall, around which a counter and shelves
        hold kitchen supplies. Against the opposite wall
        is a desk with a high backed chair. Built into a
        nook behind you is your bed, the bedding is
        slightly rumpled.
"""

text = """Lorem ipsum dolor sit amet, consectetur 
          incididunt ut labore et dolore magna """

print(text)

text = "Lorem ipsum dolor sit amet, consectetur " + "incididunt ut labore et dolore magna "

text = ("Lorem ipsum dolor sit amet, consectetur "
        "incididunt ut labore et dolore magna ")

words = [
    "apple",
    "bear",
    "tree"
    "walrus",
    "purple"
]

from pprint import pprint
pprint(words)

print(text)