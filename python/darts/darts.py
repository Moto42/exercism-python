import math


def distance_from_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def distance_to_score(distance):
    if distance > 10:
        return 0
    if distance > 5:
        return 1
    if distance > 1:
        return 5
    return 10

def score(x, y):
    distance = distance_from_center(x, y)
    return distance_to_score(distance)
