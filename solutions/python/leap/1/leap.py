def leap_year(y):
    # if y % 4 != 0:
    #     return False
    # elif y % 100 != 0:
    #     return True
    # else:
    #     return y % 400 == 0
    return (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))