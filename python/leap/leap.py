"""
is a year a leap year? what is time? how do birds know our fears?
"""
def leap_year(year):
    """
    returns if a year is a leap year
    :param year: year in question
    :return: boolean - true if leap year
    """

    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    return divisible_by_4 and (not divisible_by_100 or divisible_by_400)
