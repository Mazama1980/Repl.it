"""Exercise 68.(Countdown With Args Exercise)
 Write a program which counts down from 3 by default, 
 or from the number passed by the first argument if present. 
 Use time.sleep() to pause for a second between printing each number.

 If there is a second argument, save it to the variable finish_message, and
 print it after the end of the countdown.
 
 Example:
    $ python countdown.py 10 "Happy New Year!"
    10...
    9...
    8...
    7...
    6...
    5...
    4...
    3...
    2...
    1...

    Happy New Year!

    $ python countdown.py 3 "Go team!"
    3...
    2...
    1...

    Go team!
 """

import sys
import time 
def countdown():
    print("sys.argv:", sys.argv)
    count = 3
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    print(f'The count is: {count}')

    i = count
    while i > 0:
        print(f"countdown: ", i)
        time.sleep(1)
        i -= 1
    if len(sys.argv) > 2:
        finish_message = sys.argv[2]
        print(finish_message)


countdown()
