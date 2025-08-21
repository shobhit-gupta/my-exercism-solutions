def isTriangle(sides):
    a, b, c = sorted(sides)
    # _Strict_ triangle inequality ensures `a > 0` implicitly given a <= b <= c.
    return a + b > c

def unique_sides(sides):
    return len(set(sides))

def equilateral(sides):
    return isTriangle(sides) and unique_sides(sides) == 1


def isosceles(sides):
    return isTriangle(sides) and unique_sides(sides) <= 2


def scalene(sides):
    return isTriangle(sides) and unique_sides(sides) == 3
