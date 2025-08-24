def is_armstrong_number(n):
    if n < 10: return True
    s = str(n)
    p = len(s)
    return n == sum(int(x)**p for x in s)
