"""Textbased adventure game. https://alissa-huskey.github.io/python-class/exercises/adventure.html 

"""

from pprint import pprint


ITEMS = [
    {
        "name": "crystal ball",
        "desc": "it glows faintly",
        "price": 5,
    },
    {
        "name": "short dagger",
        "desc": "antler handle with double edged blade",
        "price": 22,
    },
]
def do_quit():
    print("Goodbye!")
    quit()

def main():
    print("Welcome!")
    while True:
        reply = input(">")
        if reply == "quit":
            do_quit()
        else:
            print("No such command.")
            continue


    
        

if __name__ == "__main__":
    main()
    
