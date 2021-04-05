"""
INTEGER RIGHT TRIANGLES
"""
import math


if __name__ == "__main__":
    """
    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
    """
    print("Problem 39: Integer right triangles")

    # the minimum perimeter is 12 for {3 4 5 triangle}
    answer = 12
    max_solutions = 0
    for p in range(12, 1001):
        solutions = 0
        for a in range(1, p // 3):
            for b in range(a, p // 2):
                perim = a + b + math.sqrt(a**2 + b**2)
                if perim == p:
                    solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            answer = p
    print(answer)
