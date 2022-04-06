from testing_lesson import endgame, add, greeting, subtract, multiply
import pdbr

def test_add():
    result = add(1,2)
    assert result == 3, f"{result} should be 3"
    
def test_endgame():
    assert endgame(False) == f"You lost. Better luck next time!"

# def test_greeting():
#     assert greeting("nila") == "Welcome Nila.", 'should return "Welcome Nila."'
#     assert greeting("NILA") == "Welcome Nila.", 'should return "Welcome Nila."'
#     text = greeting(".")
#     assert text == "Welcome.", f'should return "Welcome." but is: {text!r}'
#     text = greeting("nila huskey")
#     assert text == "Welcome Nila Huskey.", f'should return "Welcome, Nila Huskey."'

def test_greeting_with_name():
    assert greeting("nila") == "Welcome Nila.", 'should return "Welcome Nila."'

def test_greeting_with_allcaps_name():
    assert greeting("NILA") == "Welcome Nila.", 'should return "Welcome Nila."'

def test_greeting_without_name():
    text = greeting(" ")
    assert text == "Welcome.", f'should return "Welcome." but is: {text!r}'

def test_greeting_with_multiword_name():
    text = greeting("nila huskey")
    assert text == "Welcome Nila Huskey.", f'should return "Welcome, Nila Huskey."'

def test_subtract():
    value = subtract(5, 1)
    assert value == 4, f"subtract(5, 1) should equal 4 but is: {value}"

def test_multipy():
    total = multiply(2,2)
    assert total == 4, f'"should total 4: {total}"'