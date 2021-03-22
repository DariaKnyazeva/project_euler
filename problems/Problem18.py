"""
MAXIMUM PATH SUM I
"""
import unittest


def get_triangle_path_sum(triangle):
    # deprecated
    # Tried to choose the path by selecting the biggest neighbor
    summa = triangle[0][0]
    next_index = 0
    for i in range(1, len(triangle)):
        try:
            if triangle[i][next_index] > triangle[i][next_index + 1]:
                summa += triangle[i][next_index]
                # print(triangle[i][next_index])
            else:
                summa += triangle[i][next_index + 1]
                # print(triangle[i][next_index + 1])
                next_index += 1
        except IndexError:
            if triangle[i][next_index] > triangle[i][next_index - 1]:
                summa += triangle[i][next_index]
                # print(triangle[i][next_index])
            else:
                summa += triangle[i][next_index - 1]
                # print(triangle[i][next_index - 1])
                next_index -= 1
    return summa


class Node:
    """
    Represents tree node.
    data is the numeric value,
    left and right are the pointers to the corresponding nodes
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        left = self.left.data if self.left else ""
        right = self.right.data if self.right else ""
        return f"{self.data}: <{left}> <{right}>"


class Tree:

    def __init__(self, triangle):
        """
        @param triangle 2-dimentional array, for example
        triangle = [
            [3, ],
            [7, 4, ],
            [2, 4, 6, ],
            [8, 5, 9, 3, ],
        ]
        """
        self.nodes = {}

        for row_number, row in enumerate(triangle):
            for index, val in enumerate(row):
                self.nodes[f"{row_number}-{index}"] = Node(val)

        for row_number, row in enumerate(triangle):
            for index, val in enumerate(row):
                node = self.nodes[f"{row_number}-{index}"]
                if row_number + 1 == len(triangle):
                    continue
                node.left = self.nodes[f"{row_number+1}-{index}"]
                node.right = self.nodes[f"{row_number+1}-{index+1}"]

        self.root = self.nodes['0-0']

    def max_path_sum(self, root, res=[-1]):
        # Base Case
        if root is None:
            return 0

        # Find maximumsum in left and righ subtree. Also
        # find maximum root to leaf sums in left and righ
        # subtrees ans store them in ls and rs
        ls = self.max_path_sum(root.left, res)
        rs = self.max_path_sum(root.right, res)

        # If both left and right children exist
        if root.left is not None and root.right is not None:
            # update result if needed
            res[0] = max(res[0], ls + rs + root.data)

            # Return maximum possible value for root being
            # on one side
            return max(ls, rs) + root.data

        # If any of the two children is empty, return
        # root sum for root being on one side
        if root.left is None:
            return rs + root.data
        else:
            return ls + root.data


class Problem18Test(unittest.TestCase):
    def test_triangle_path(self):
        triangle = [
            [3, ],
            [7, 4, ],
            [2, 4, 6, ],
            [8, 5, 9, 3, ],
        ]

        tree = Tree(triangle)
        self.assertEqual(tree.max_path_sum(tree.root), 23)


unittest.main()


if __name__ == "__main__":
    """
    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """
    print("Problem 18: Maximum path sum")
    triangle = [
        [75, ],
        [95, 64, ],
        [17, 47, 82, ],
        [18, 35, 87, 10, ],
        [20, 4, 82, 47, 65, ],
        [19, 0, 23, 75, 3, 34, ],
        [88, 2, 77, 73, 7, 63, 67, ],
        [99, 65, 4, 28, 6, 16, 70, 92, ],
        [41, 41, 26, 56, 83, 40, 80, 70, 33, ],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29, ],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, ],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, ],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, ],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, ],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23, ],
    ]

    tree = Tree(triangle)
    print(tree.max_path_sum(tree))
