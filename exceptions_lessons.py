def raising_exceptions():
    """Demonstrate raising an exception."""
    # create an exception object with your own exception message
    ex = Exception("Hey now, that's not right!")
    
    # raise that exception, (sometimes called "throwing an error")
    # which is the same thing that Python does when it encounters
    # an error in your code
    raise ex

def catching_exceptions():
    """Demonstrate a try/except block."""
    a = 1
    b = 0

    try:
        # this is the line that may raise an exception
        # (depending on the values of a and b)
        result = a / b
    # BaseException allows you to catch any exception type, even if you do not know which one it might be
    # Or you can use the specific exception type (like ValueError) to only catch that kind of exception
    # ex is the variable name that you give to the exception object (so that you can look at the exception type and message)
    except BaseException as ex:
        # you can use a breakpoint here to debug the error
        breakpoint()
        print("Uh oh, it looks like either a or b is zero.")
        return

    # With the code written as it is, you will only get to this line if there is an exception raised and caught above, because we return when catching the exception
    print(f"{a}/{b}={result}")

# this is a useful technique for debugging
# here we are calling out raising_exceptions() function, which raises an exception
# then we catch it, and add a breakpoint so we can see the exception we raised
try:
    raising_exceptions()
except BaseException as ex:
    breakpoint()
    # note: when the last line in a block is a breakpoint,
    # sometimes the debugger does not behave correctly and stop at the right place
    # adding a line with ... or pass under the breakpoint will
    # ensure the debugger stops where we want
    ...
    
catching_exceptions()