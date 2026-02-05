from math import isqrt

def classify(n: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param n: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if n == 1:
        return "deficient"  # aliquot sum = 0

    s = 1  # 1 is a proper divisor for all n > 1
    r = isqrt(n)

    # iterate i up to sqrt(n), add the divisor pair (i, n//i)
    # skip adding sqrt twice for perfect squares
    for i in range(2, r + 1):
        if n % i == 0:
            q = n // i
            s += i
            if q != i:
                s += q
            if s > n:
                return "abundant"  # early exit

    return "perfect" if s == n else "deficient"
