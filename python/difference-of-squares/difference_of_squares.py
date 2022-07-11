import functools


def summer(acc, cur):
    return acc + cur


def squarm(acc, cur):
    return acc + cur ** 2


def square_of_sum(number):
    sum_num = functools.reduce(summer,range(1,number + 1), 0)
    return sum_num ** 2


def sum_of_squares(number):
    return functools.reduce(squarm, range(1, number + 1), 0)


def difference_of_squares(number):
    return abs(sum_of_squares(number) - square_of_sum(number))
