"""Textbased adventure game."""

from pprint import pprint


ITEMS = [
    {
        "name": "crystal ball",
        "desc": "it glows faintly",
        "price": 5,
    },
    {
        "name": "short dagger",
        "desc": "antler handle with double edges",
        "price": 22,
    },
]

def main():
    # pprint(ITEMS)
    for item in ITEMS:
        print(
            format(item["name"], "<14s"),
            format(item["desc"], "<33s"),
            format(item["price"], ">2d"),
            "gems",
        )
        

if __name__ == "__main__":
    main()
