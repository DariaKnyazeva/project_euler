"""
LATTICE PATHS
"""
from utils.combinatorics import c_n_k


if __name__ == "__main__":
    """
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
    """
    print("Routes in 2x2 grid:")
    print(c_n_k(4, 2))
    print("Routes in 20x20 grid:")
    print(c_n_k(40, 20))
