"""
Module for the old "How many grains on a chessboard" problem
"""


def sanity_check(number):
    """
    Sanity check number passed into functions
    :param number: int - number to check
    :return: none
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

def square_grains(number):
    """
    Returns number of grains on a square
    :param number: int - the number of the square
    :return: int - the number of grains
    """
    return 2 ** (number-1)


def square(number):
    """
    return number of grains on a given square

    :param number: int - the number of the square
    :return: int - the number of grains on that square
    """
    sanity_check(number)
    return square_grains(number)


def total():
    """
    Return the total grains on the board.
    :return: int - the total grains on the board.
    """
    out = 0
    for i in range(1, 65):
        out += square_grains(i)
    return out
