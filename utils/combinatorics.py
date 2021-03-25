import math


def c_n_k(n, k):
    """
    Returns number of combinations of n by k
    """
    assert k <= n
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))
