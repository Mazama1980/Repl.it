"""Textbased adventure game. https://alissa-huskey.github.io/python-class/exercises/adventure.html 
continue with 2.1 B.2

"""

from pprint import pprint

DEBUG = True
ITEMS = {
    "crystal ball": {
        "key": "crystal ball",
        "name": "it glows faintly",
        "description": "all it does is glow faintly; could be used in dark places",
        "price": -5,
    },
    "short dagger": {
        "key": "short dagger",
        "name": "antler handle with double edged blade",
        "description": "hardened steel, the blade is sharp on both sides, polished antler bone handle, about 10 inches in length, comes with a sheath",
        "price": -22,
    },
}

def debug(message):
    if DEBUG == True:
        print("Debug: ", message)

def do_shop():
    print("Items for sale")
    for k, item in ITEMS.items():
        print(k, item["name"], item["description"])
    
def do_go(args):
    print("Trying to go: ", args)

def do_quit():
    print("Goodbye!")
    quit()

def main():
    debug("Hello")
    print("Welcome!")
    while True:
        reply = input(">").strip()
        if reply == "quit":
            do_quit()
        elif reply == "shop":
                do_shop()
        else:
            print("No such command.")
            continue
      

if __name__ == "__main__":
    main()
    
