from Spaceman import *

def test_is_word_guessed():
    assert is_word_guessed('axe', ['a','z','e']) == False
    assert is_word_guessed('axe', ['a','x','e']) == True
    
def test_get_guessed_word():
    assert get_guessed_word('axe',['a','x','c']) ==  "ax _"
    assert get_guessed_word('axe',['a','x','e']) ==  "axe"

def test_is_guess_in_word():
    assert is_guess_in_word('v','axe') == False
    assert is_guess_in_word('x','axe') == True
