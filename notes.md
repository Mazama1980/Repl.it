# Notes

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