"""Ham it up"""


def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    ham_distance = 0
    for index, nuc in enumerate(strand_a):
        if nuc != strand_b[index]:
            ham_distance += 1
    return ham_distance
