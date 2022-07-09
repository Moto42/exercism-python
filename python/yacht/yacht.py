def yacht(dice):
    return 50 if dice.count(dice[0]) == 5 else 0


def sum_of(dice):
    result = 0
    for die in dice:
        result += die
    return result


def ones(dice):
    return 1 * dice.count(1)


def twos(dice):
    return 2 * dice.count(2)


def threes(dice):
    return 3 * dice.count(3)


def fours(dice):
    return 4 * dice.count(4)


def fives(dice):
    return 5 * dice.count(5)


def sixes(dice):
    return 6 * dice.count(6)


def full_house(dice):
    dice.sort()
    num_a = dice.count(dice[0])
    num_b = dice.count(dice[-1])
    valid = (num_a == 3 and num_b == 2) or (num_a == 2 and num_b == 3)
    return sum_of(dice) if valid else 0


def four_of_a_kind(dice):
    dice.sort()
    num_a = dice.count(dice[0])
    num_b = dice.count(dice[-1])
    value = dice[0] if num_a >= 4 else dice[-1] if num_b >= 4 else 0
    return value * 4


def little_straight(dice):
    result = 30
    for i in [1, 2, 3, 4, 5]:
        if i not in dice:
            result = 0
            break
    return result


def big_straight(dice):
    result = 30
    for i in [2, 3, 4, 5,6]:
        if i not in dice:
            result = 0
            break
    return result


def choice(dice):
    return sum_of(dice)


# Score categories.
# Change the values as you see fit.
YACHT = yacht
ONES = ones
TWOS = twos
THREES = threes
FOURS = fours
FIVES = fives
SIXES = sixes
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = choice

def score(dice, category):
    return category(dice)
