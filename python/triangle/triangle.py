def triangle_inequality(sides):
    [side_a, side_b, side_c] = sides
    ab_c = side_a + side_b > side_c
    bc_a = side_b + side_c > side_a
    ca_b = side_c + side_a > side_b
    return ab_c and bc_a and ca_b


def equilateral(sides):
    """
    is triangle equilateral?
    :param sides:
    :return:
    """
    [side_a, side_b, side_c] = sides
    return side_a == side_b and\
        side_b == side_c and\
        side_c == side_a and\
        0 not in sides and triangle_inequality(sides)


def isosceles(sides):
    [side_a, side_b, side_c] = sides

    return 0 not in sides and\
        triangle_inequality(sides) and\
        (
            side_a == side_b or
            side_b == side_c or
            side_c == side_a
        )


def scalene(sides):
    [side_a, side_b, side_c] = sides
    a_b = side_a != side_b
    b_c = side_b != side_c
    c_a = side_c != side_a
    return a_b and\
        b_c and\
        c_a and\
        triangle_inequality(sides) and\
        0 not in sides
