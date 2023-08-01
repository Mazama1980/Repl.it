****
# To Do

## future to learn / do

[x] add annotations and docstrings to 1-2 functions until they are all done
[ ] respond to the TODO comments above some functions and fix the stuff
[ ] for at least some, add an "Args:" section (to get practice)
[ ] add tests for
    [ ] place_has()

### Part 10.2 (tests)

[x] write a test_place_can_true() test
[x] in it, make a fake place that has a "can" key that contains a fake command string
[x] call it with that string
[x] assert that it is true

[x] write a test_place_can_false() test
[x] figure out how to write this test

[x] do 10.2 A
[x] do 10.2 C
[x] write test for do_buy() command
[-] do 10.3
[x] finish do_buy() (to add the message about how many gems the player has and
    the price of the item)
[x] Fix inventory_change() as per failing test: test_inventory_change_with_negative_quantity
[x] write a test_do_buy_actually_buy() for when the user really buys it
[x] finish do_buy() to actually buy the item
[x] 10.4 do the string formatting for the do_shop function list that prints out
[ ] add tests for any do_*() functions that deal with items to include quotes in
    the key name, for example do_examine()
[x] change tests to reflect changes made to 'key' and 'name' in the game functions
[x] change your all your "name" keys in your ITEMS dictionary to be "summary"
[x] go through all your do_*() functions to see where item["name"] is used, and see if you meant to use "name" or "summary"
[x] change formatting on inventory
[x] add tests for do_examine:
    [x] when item is in the current place
    [x] when item is in inventory
    [x] when item not in inventory or the current place
[x] Look at the way items are printed in the following commands, and check that
    you are using the item["name"], item["key"], item["summary"], and
    item["description"] correctly
    [x] do_examine()
    [x] do_take()
    [x] do_buy()
    [x] do_drop
[x] Do 10.4 C
[x] Do 10.4 D first test is done. Need to implement code in do_examine

### Reorganize adventure.py

Proposed order of file is:

1. docstring
2. imports
3. global variables
4. functions: (each section in alphabetical order)
   1. utility functions (all except main and do_*)
   2. command functions (do_*)
   3. main()

### Aliases function

[x] write a test_setup_aliases() test
    [x] ...
[x] write a function setup_aliases() 
    [x] write a for loop iterating over ITEMS.items() getting two variables `key` (str) and `item` (dict)
        [x] nest a for loop iterating over item['aliases'] (list) getting the variable `alias` (str)
            [x] add to ITEMS_ALIASES (dict) with the key `alias`(str) and the value `item` (dict) 
    [x] add to ITEMS_ALIASES with the key `key` (str) and the value `item` (dict)
[x] add ITEMS_ALIASES to tests and call setup_aliases() in tests (Alissa to figure this part out)
[x] add 'aliases' key to each item where needed in the ITEMS dicionary
    [x] add a list of possible words for each item as a dictionary in the 'aliases' key   
[x] make a new global dicitionary ITEMS_ALIASES that's empty    
[x] write or modify a test_get_item() test to reflect pulling from ITEMS_ALIASES
    [x] make sure it works with the original item key, any alias in the aliases list, and for items with no "aliases" key
[x] change the get_item() function to get items from ITEMS_ALIASES instead of ITEMS
[x] call the function setup_aliases() in main()
[ ] might need to change some tests if any of them broke

```python
# imaginary ITEMS dict
ITEMS = {
    "crystal ball": {
        "key": "crystal ball",
        "aliases": ["ball", "globe"],
        "name": "Crystal ball",
        "summary": "a faintly glowing ball",
        "description": "all it does is glow faintly; could be used in dark places.",
        "price": -5,
    },
    "book": {
        "key": "book",
        "name": "Book",
        "summary": "Diary of a wimpy dragon",
        "description": "A soft leather bound book laying on the desk at home. There may be useful information in it.",
        "can_take": True,
    },
}

# before
ITEMS_ALIASES = {}

def setup_aliases():
    ...

crystal_ball = ITEMS.get("crystal ball")
book = ITEMS.get("book")

# AFTER (but modified by setup_aliases(), not hard-coded)
ITEMS_ALIASES = {
    "crystal ball": crystal_ball,
    "ball": crystal_ball,
    "globe": crystal_ball,
    "book": book,
}

# if the user types any of these, it should work
# buy "crystal ball"
# buy globe
```
```python
###############################################
# example of how to test an expected exception
###############################################

# a function that raises an exception sometimes
def func(something=None):
    if not something:
        # ValueError is the exception class
        raise ValueError("you can't do that!")
    return something

# a normal test, where the exception is not raised
def test_func():
    result = func("hello")
    assert result == "hello"
    
# test for the expected exception
def test_func_when_no_arg():
    # put the exception class inside the pytest.raises() parens
    # ex is an object containing the exception that was raised
    with pytest.raises(ValueError) as ex:  # "for the following code, we expect an exception to be raised"
        # the code that you expect to raise the exception goes here
        func()

    # ex.value is the actual exception that was raised
    # convert it to a string to see the exception message
    assert str(ex.value) == "you can't do that!"

#########################################################
# example of with statement to open a file
#########################################################

# without a with statement
fp = open("something.txt")
text = fp.read()
fp.close()
print(text)

# using a with statement
with open("something.txt") as fp:   # "for as long as this file is open"
    text = fp.read()

print(text)
