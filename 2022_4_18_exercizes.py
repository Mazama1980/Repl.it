# [ ] write a function called max_num that takes a list of numbers and reeturns
#     the highest number 

# letters = "xyz"
# letters.upper() + str(123)
# "xyz".upper() + str(123)

# from random import randint

# number = randint(1, 100)

# if number > 80:
#     print("you got a high number!")

# def say(message):
#     # message = ""
#     return "hello " + message

# print(say("there"))

# text = say("silly face")
# print(text)

# say("you")
# say("somewhere")

def max_num(values):
    # breakpoint()
    for i, x in enumerate(values):
        y = values[i + 1]
        breakpoint()
        pass
        # y = values
        # if x > y:
        #     return x
        # else:
        #     return y

# max_num([1, 2, 3])
# max_num([4, 5, 6])

def test_max_num():
    """Call the max_num() function with a list of numbers for the argument, then
    test that the returned result is the highest number."""
    numbers = [10, 20, 30, 40, 50]
    highnum = max_num(numbers)
    assert highnum == 50, f'The highest number should be 50'

def test_max_num_with_negatives():
    numbers = [-10, -5, -1]
    highnum = max_num(numbers)
    assert highnum == -1, "The highest number should be -1"