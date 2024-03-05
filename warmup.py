import random

WINNING_NUMBER = 5

def roll_dice(sides):
    this_roll = random.randint(1, sides+1)
    # print(f"You rolled: {this_roll}")
    return this_roll

def main():
    greeting = 'Hello World'
    print(greeting)
    number = random.randint(0,101)
    print(number)
    if number < 50:
        print(f'Oh no! The number {number} is less than 50. You have to put your finger up your nose.' )
    elif number < 75:
        print(f'For this number {number} you get to cross your eyes.')
    else:
        print(f'When the number, which is {number}, gets above 75 you can now wriggle your ears.')
    for i in range(20, 26):
        print(i)

    my_number = roll_dice(6)

    if my_number == WINNING_NUMBER:
        print(f"You win! The winning roll is: {WINNING_NUMBER}")
    elif my_number < WINNING_NUMBER:
        print(f"Your roll {my_number} is too low!")
    elif my_number > WINNING_NUMBER:
        print(f"Your roll {my_number} is too high!")

    my_other_number = roll_dice(8)

# main()
    
# write a function named can_drink
# it should take one argument, the age
# then return True if the age is over 21, or return False if not
# call it (outside of the function)and print the result
def can_drink(age):
    if age >= 21:
        return True
    else:
        return False

        
can_harper_drink = can_drink(7)
if can_harper_drink == True:
    print('Here, Harper, have a beer.')
else:
    print('Here is your juice box.')

can_whitney_drink = can_drink(36)
if can_whitney_drink == True:
    print("Here is some of Jeremy's mead.")
else:
    print("Have some water.")
    
def dictionary_review():
    # basic dict
    inventory = {
        "apples": 5,
        "hats": 1,
    }
    # accessing an item
    print(inventory["apples"])  # 5
    
    # changing an item
    inventory["hats"] = 2
    print(inventory["hats"])    # 2
    
    # add an item
    inventory["bread"] = 3
    print(inventory["bread"])    # 3
    
    # nested dictionary
    addresses = {
        "alissa": {
            "name": "alissa",
            "city": "Denver, CO",
        }
    }

    print(addresses["alissa"])          # {"name": "alissa", "city": "Denver, CO"}
    print(addresses["alissa"]["city"])  # "Denver, CO"


    # another way to do a nested dictionary
    addresses = {}
    addresses["alissa"] = {
        "name": "alissa",
        "city": "Denver, CO",
    }

    # nested list (list that contains dictionaries that contain a list)
    menu = [
        { # 0
            "meal": "sandwich",
            "price": 7.75,
            "ingredients": ["bread", "cheese", "mayo", "turkey"],
        },
        { # 1
            "meal": "pizza",
            "price": 5,
            "ingredients": ["dough", "cheese", "sauce"],
        }
    ]
    print(menu[0]["ingredients"][1])    # cheese
    
    
    
# Your task, should you choose to accept it:
# Write one or more tests for your can_drink() function
def test_can_drink(capsys):
    # Given: if age is >= 21
    # When: call can_drink() with an age arguement >= 21
    result = can_drink(21)
    # Then: the result will return True
    assert result is True
