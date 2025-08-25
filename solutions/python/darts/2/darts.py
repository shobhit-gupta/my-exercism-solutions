def score(x, y):
    r2 = x*x + y*y
    return (r2<=1)*5 + (r2<=25)*4 + (r2<=100)
