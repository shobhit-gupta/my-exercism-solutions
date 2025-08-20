def isTriangle(sides):
    a, b, c = sorted(sides)
    sides_non_zero = (a > 0)
    triangle_inequality = (a + b >= c)
    return sides_non_zero and triangle_inequality

def unique_sides(sides):
    return len(set(sides))

def equilateral(sides):
    return isTriangle(sides) and unique_sides(sides) == 1


def isosceles(sides):
    return isTriangle(sides) and unique_sides(sides) <= 2


def scalene(sides):
    return isTriangle(sides) and unique_sides(sides) == 3
