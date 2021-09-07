"""Exercise 43 (Shapes Dictionary)

Create a dictionary assigned to the variable shapes that uses shape names (like "square" or "triangle") for keys and the number of sides (like 4 and 3) for values.

Print the dictionary."""

def objects():
    shapes= {
        "triangle": 3,
        "square": 4,
        "rectangle": 4,
        "pentagon": 5,
        "hexagon": 6,
        "octogon": 8,

    }
    # print("A square has", shapes["square"], "sides.")
    # print("A rectangle has", shapes["rectangle"], "sides.")
    answer = input("What shape would you like to know the number of sides for it? ")
    sides = shapes.get(answer)
    if sides:
        print("The shape", answer, "has", sides, "sides.")
    else:
        print("Sorry I do not know that shape:", answer)
objects()