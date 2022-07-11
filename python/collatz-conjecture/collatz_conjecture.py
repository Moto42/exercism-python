def collatz(number):
    if number % 2 == 0:
        number = number / 2
    else:
        number = 3 * number + 1
    return number


def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps_taken = 0
    while number != 1:
        steps_taken += 1
        number = collatz(number)
    return steps_taken
