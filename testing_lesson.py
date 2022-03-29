def add(a,b):
    total = a + b
    return total

def subtract(a, b):
    return a - b

def multiply(a,b):
    return a * b
 
def endgame(is_winner):
    """Return a string to tell the player if they won or lost."""
    if is_winner:
        return "Congratulations, you won!"
    else:
        return "You lost. Better luck next time!"

def greeting(name):
    """Return a welcome message string, including formatted name unless it's blank."""
    name = name.strip().title()
    if not name:
        return "Welcome."
    else:
        return f"Welcome {name}."



def main():
    print("oh hai there")
    reply = input("what do you want to do today?")

if __name__ == "__main__":
    main()