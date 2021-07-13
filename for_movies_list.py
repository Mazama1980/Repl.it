"""For Loops: Syntax
    Exercise 27 (Movies)"""
"""Iterate over a list of movies and print each one out using a for loop."""


def movie():

    movies = [
        "LOTR", 
        "the Black Stallion",
        "Amelie",
        "Independence Day",
        "Star Trek",
        "Star Wars",
    ]
    for name in movies:
        print(name)


"""Iterables and iterators.
Exercise 28 (Iterators) in a python shell:
    Create a list containing the letters in your name assigned to the variable letters.

    Convert the list to an iterator using the iter() function and assign it to the variable letters_iterator.

    Keep calling next() with the argument letters_iterator until you encounter a StopIteration exception.
"""
def name():
    letters = [
        "N",
        "I",
        "L",
        "A",
    ]
    letters_iterator = iter(letters)
    next(letters_iterator)


"""Exercise 29 (Game Characters)

    1.Make a list of game character roles.

    2.write a while loop

        1.Convert the list to an roles_iter iterator using the iter() function

        2.Make a while loop with the condition True

        3.Get each role element from the roles_iter by calling next()

        4.Print the role

        5.Suppress the error with a try-except block

    3.write a for loop

        1.Make a for loop with the variable name role and the iterable roles

        2.Print the role.
    """
def game_roles():
    roles = [
        "Warrior",
        "Wizard",
        "Hunter",
        "Thief",
        "Healer",
    ]
    roles_iter = iter(roles)
    while True:
        try:
            name = next(roles_iter)
        except StopIteration:
            break
        print(f'Game Character Role: {name}')

    for name in roles:
        print(f'Game character role {name}')


"""Exercise 30 (Game Tools)

    1.Make a dict of game character tools, where the key is the role and the value is a tool.

    2.write a while loop

        1.Convert tools.items() to an tools_iter iterator using the iter() function

        2.Make a while loop with the condition True

        3.Get each role and tool element from the tools_iter by calling next()

        4.Print the "A roles favorite tool is their trusty: tool."

        5.Suppress the error with a try-except block

3.write a for loop

        1.Make a for loop with the variable name tool and the iterable tools

        2.Print the tool.
"""
def character_tools():
    tools = {
        "Warrior": "Sword",
        "Wizard": "Staff",
        "Hunter": "Crossbow",
        "Thief": "Rope",
        "Healer": "Herbs",
    }
    tools_iter = iter(tools.items())
    while True:
        try:
            role, tool = next(tools_iter)
        except StopIteration:
            break
        print(f'This is the tool of a {role}: {tool}')
    
    for role, tool in tools.items():
        print(f'A weapon of a {role} is a {tool}')
        
# character_tools()
# game_roles()
# name()
# movie()