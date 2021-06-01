""" 1. Write a function named welcome that prints "Welcome to coding class!
    2. Write a function called letter_count that takes one argument word and
       prints There are __ characters in the word '___'.
    3. Write a function named is_vowel that returns True if a character is a
       vowel, and False otherwise.
    4. Write a function 'tip' that takes two arguments, 'cost' and 'percent' and
       returns the tip amount.
"""
def welcome():
    """Write a function named welcome that prints "Welcome to coding class!"""
    greeting = ("Welcome to coding class!")
    print(greeting)

def letter_count(word):
    """Write a function called letter_count that takes one argument word and
       prints There are __ characters in the word '___'. Conditional Statement Lesson"""
    phrase = len(word)
    print(f"There are {phrase} characters in the word {word}.")

def is_vowel(letter):
    """Write a function named is_vowel that returns True if a character is a
       vowel, and False otherwise."""
    letter = letter.lower()
    if letter in ["a","e","i","o","u"]:
        return True
    else:
        return False


def tip(cost, percent):
    """Write a function 'tip' that takes two arguments, 'cost' and 'percent' and
       returns the tip amount."""
    return cost, percent
    

    

 
welcome()
letter_count("happy")

amount = tip(100,20)
print("A 20% tip of $100 is:", amount)


is_it = is_vowel("a")
print("is 'a' a vowel?:", is_it)

is_it = is_vowel("b")
print("is 'b' a vowel?:", is_it)

is_it = is_vowel("E")
print("is 'E' a vowel?:", is_it)

is_it = is_vowel("hello")
print("is 'hello' a vowel?:", is_it)

is_it = is_vowel("abalone")
print("is 'abalone' a vowel?:", is_it)