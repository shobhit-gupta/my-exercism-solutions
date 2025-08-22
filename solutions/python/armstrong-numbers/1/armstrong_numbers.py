def is_armstrong_number(n):
    s = str(n)
    p = len(s)
    return n == sum([int(x)**p for x in s])
