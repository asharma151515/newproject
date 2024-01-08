"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""
import doctest

from Prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_Sentence(phrase):
    """
    Format a phrase as a sentence,starting with a capital and ending with a full stop.

    >>> format_Sentence('hello')
    'Hello.'
    >>> format_Sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_Sentence('This is a test')
    'This is a test.'
    """
    sentence = phrase.capitalize()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # ...
    # assert test check if Car sets the fuel correctly (using default value)
    test_car = Car()
    assert test_car.fuel == 0, "Car does not set fuel correct (default)"

    # assert test to check if Car sets the fuel correctly (using custom value)
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not ser fuel correct (custom value)"

    run_tests()


doctest.testmod()
