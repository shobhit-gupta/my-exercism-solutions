def isTriangle(sides):
    a, b, c = sides
    sides_non_zero = (a > 0) and (b > 0) and (c > 0)
    triangle_inequality = (a + b >= c) and (b + c >= a) and (a + c >= b)
    return sides_non_zero and triangle_inequality

def equilateral(sides):
    a, b, c = sides
    return isTriangle(sides) and (a == b) and (b == c)


def isosceles(sides):
    a, b, c = sides
    return isTriangle(sides) and ((a == b) or (b == c) or (c == a))


def scalene(sides):
    a, b, c = sides
    return isTriangle(sides) and (a != b) and (b != c) and (c != a)
