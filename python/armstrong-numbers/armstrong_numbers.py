import functools


def is_armstrong_number(number):
    digits = [int(char) for char in str(number)]
    num_digits = len(str(number))

    def reducer(acc, cur):
        return acc + (cur ** num_digits)

    armstrongified = functools.reduce(reducer, digits, 0)
    return number == armstrongified
