"""Exercise 39 (Word calculator)

Make a dictionary of numbers where the keyword is a word (like "one") and the value is an integer (like 1). 
   Assign it to the variable numbers.

Write an add() function that takes two string arguments, adds together the value in the numbers dictionary 
   associated with those keys, and returns the result."""



numbers = {"one": 1,
           "two": 2,
           "three": 3,
           "four": 4,
}
def add (a,b):
    """add the value of two number strings.
    add("one", "three")"""
    print("a is:", a)
    print("b is:", b)
    print("numbers[a] is:", numbers[a])
    print("numbers[b] is:", numbers[b])
    total = numbers[a] + numbers[b]
    print("total is:", total)
    return(total)

results = add("one", "three")
print("results is:", results)

results = add("two", "four")
print("results is:", results)

print('numbers["three"] is:', numbers["three"])


"""Exercise 40"""
POINTS = {"A": "1",
          "E": "1",
          "I": "1",
          "L": "1",
          "N": "1",
          "O": "1",
          "R": "1",
          "S": "1",
          "T": "1",
          "U": "1",
          "D": "2",
          "G": "2",
          "B": "3",
          "C": "3",
          "M": "3",
          "P": "3",
          "F": "4",
          "H": "4",
          "V": "4",
          "W": "4",
          "Y": "4"
}
def score(A,E):
    total = 0
    for score in POINTS:
        outcome = POINTS[A] + POINTS[E]
        print("score is:", outcome)
        return(total)

score("A,E")