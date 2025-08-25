def score(x, y):
    r2 = x*x + y*y
    if r2 <= 1: return  10
    if r2 <= 25: return  5
    if r2 <= 100: return  1
    return 0
