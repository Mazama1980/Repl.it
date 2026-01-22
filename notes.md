# Notes

# Links
https://alissa-huskey.github.io/python-class/lessons/in-depth/functions.html#part-4-annotations

https://www.datacamp.com/tutorial/docstrings-python

This file is in [markdown](https://commonmark.org/help/).

## Iterating

If you want to iterating over both the key and the value in a dictionary, use the `.items()` method.

 For example:

```python
letters = {"a": 1, "b": 2}
for letter, place in letters.items():
	print(f"The letter '{letter}' is in the {place} place in the alphabet.")
```

The `.items()` method returns a list-like iterable, where each items is a tuple
containing the `key` and value`.

```python
letters = {"a": 1, "b": 2}
x = list(letters.items())
print(x)                    # => [("a", 1), ("b", 2)]
print(x[0])                 # => ("a", 1)
```

So when we say `for letter, place in letters.items()`, that is like setting
`letter, place` to each tuple returned by `.items()`.

```python
letters = {"a": 1, "b": 2}
letter, place = letters[0]  # letters="a" ; place=1
```

If you iterate over a list, you only get one item each time, so you only need
one variable in your for loop. 

```python
numbers = [1, 2, 3]

for number in numbers:
	# like saying number = numbers[_] ; where _ is each index number
	print(number)
```

Unless each item in your list is an iterable of the same length.

```python
pets = [
	("Gizmo", "dog", 8),
	("Mocha", "dog", 8),
	("Cinder", "cat", 18),
]
```

Then you can use just one varible, which will assign that varible to the whole
iterable.

```python
for pet in pets:
	# like saying pet = pets[_] ; where _ is each index number
	... # pet=("Gizmo", "dog", 8) the first time
```
	
Or use multiple variales to assign to each item in that child iterable.

```python
for name, species, age in pets:
	# like saying name, species, age = pets[_] ; where _ is each index number
	... # name="Gizmo", species="dog", age=8 the first time
```
## NONETYPE Error

Add the empty list brackets as a second
     argument so if a place doesn't have a 'persistent_items' key then it can continue instead
     of getting a NONETYPE error
```python
 items = new_place.get("persistent_items", [])
    for item in items:
      place_add(item)
```
## Key Error

 When you get the KeyError use the `.get()` method so that the program can return something or `NONE`. The program is trying to find the key and value for the key; if the key does not exist then an error will occur but using `.get()` method says 'Oh well, I don't see the missing key so I will return NONE'. Be sure to use `()` instead of `[]` as it is a method.

 ## Type Error

 When you get a TypeError: 'NoneType' it is not able to do anything with the Type `NONE`.

 ```python
 for key in place.get('items'):
    # this line of code will not work. It is trying to access 'items' in a dicionary that doesn't have any items. 
    # It is returning NONE and the 'for loop' is unable to iterate over NONE
for key in place.get('items', []):
    # Using the square brackets `[]` after 'items', creates an empty list that can be iterated over.
```
# True and False bools
```python
assert result 
	# this statement (assert result is assumed to be True) is the same as this:
assert result is True
	# and:
assert result == True
	# however, for False you have to make the value equal False:
assert result == False
	# or:
assert result is False
```
Using parametrization to combine similiar tests: (example below)
# def test_addition_one():
#     assert 1 + 1 == 2

# def test_addition_two():
#     assert 2 + 2 == 4

# def test_addition_three():
#     assert -2 + 2 == 0

@pytest.mark.parametrize(
    ["number_one", "number_two", "result"], [
        (1, 1, 2),
        (2, 2, 4),
        (-2, 2, 0),
        (5, 5, 11),
    ]
)
def test_addition(number_one, number_two, result):
    assert number_one + number_two == result
    
```python
  randomly choosing a number of gems from the range assigned to that dragon mood
    dragon["gems"] = random.randint([20, 20])    # 1 argument: [20, 20]
    dragon["gems"] = random.randint(20, 20)      # 2 arguments: 20 and 20

    dragon["gems"] = random.randint(possible_treasure[0], possible_treasure[1]) # 2 arguments: 20 and 20
	# the astrik tells python to make each item a separate argument instead just one argument together
    dragon["gems"] = random.randint(*possible_treasure)
```
```python
    Dictionary subscription: four ways to do it
    1:ball = ITEMS["crystal-ball"] # Make a variable
    2:ball = ITEMS.get("crystal-ball") # use the .get() function with a variable

    if not ball: # You can check if item exists with .get()
        error("whatever")
        return

    print(ball["name"]) # You can subscribe which part of dictionary you want
    print(ball["summary"])

    ball["summary"]# Another way You can subscribe which part of dictionary you want

    3:ITEMS["crystal-ball"]["summary"] # subcribe a part of dictionary without a variable

    # subcribe a part of dictionary without a variable then using empty curly braces and 0 amount
    # to keep from getting errors
    4:price = ITEMS.get("crystal-ball", {}).get("amount", 0)
     total = price + something_else
```
