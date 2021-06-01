"""Functions Lessons:
    https://alissa-huskey.github.io/python-class/lessons/functions.html"""

def hr():
    """print a horizontal line"""

    print("-" * 100)

# def header(title):
#     print(title)
#     line = '-' * len(title)
#     print(line)


# header("Chapter One")
# header("Chapter Two")
# header("Chapter Three")

def header(title, symbol):
    """print title underlined by symbol

    Example:
    >>> header("Chapter One")
    Chapter One
    -----------
    """
    # Exercise 2 (header function)

    # [x]Write a header() function that takes one string parameter title and prints the title followed by a line of dashes 
    # the same length of the title, like so:

    line = symbol * len(title)
    print(title)
    print(line)

# header("Part I", "=")
# header("Chapter One", "-")



import random
def choices():
    """Returning Values
        Exercise 3 (random function)

        [x]Write a number() function to return a random number between 1 and 100.
    """
    return random.randint(1,100)
    

def main():
    number1 = choices()
    number2 = choices()
    print(f"number 1 is: {number1}")
    print(f"number 2 is: {number2}")

    product = number1 * number2
    print(f"{number1} * {number2} = {product}")


if __name__ == "__main__":
    header("Chapter One", "=")
    header("Chapter Two", "+")
    header("Chapter Three", "*")
    hr()
    choices()
    main()