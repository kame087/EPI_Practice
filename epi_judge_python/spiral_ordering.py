from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    """
    HIGH LEVEL:
        Essentially you're "deshelling" each outer shell/bound starting with top -> right -> bottom -> left
        updating the shell level (from outer top to inner top, etc) as you traverse each bound.

        "top" being the lower bound of the row count i.e. 0
        "bottom" being the upper bound of the row count i.e len(square_matrix) - 1

        "left" being the lower bound of the column count i.e. 0
        "right" being the upper bound of the column count i.e. len(square_matrix[0]) - 1
            l->  <-r
        t->[1, 2, 3]
           [4, 5, 6]
        b->[7, 8, 9]

    :param square_matrix:
    :return: result List[int]
    """
    top, bottom, left, right = 0, len(square_matrix)-1, 0, len(square_matrix[0])-1 # starting indices for each "shell"
    direction = 0 # 0: L -> R, 1: T -> B, 2: R -> L, 3: B -> T
    result = []

    while top <= bottom and left <= right:
        if direction == 0:
            # loop from left to right, while keeping top the same
            # then updating top
            for i in range(left, right+1):
                result.append((square_matrix[top][i]))
            top += 1
        elif direction == 1:
            # loop from top to bottom, while keeping right the same
            # then updating right
            for i in range(top, bottom+1):
                result.append((square_matrix[i][right]))
            right -= 1
        elif direction == 2:
            # loop from right to left, while keeping bottom the same
            # then updating bottom
            for i in range(right, left-1, -1):
                result.append(square_matrix[bottom][i])
            bottom -= 1
        elif direction == 3:
            # loop from bottom to top, while keeping left the same
            # then updating left
            for i in range(bottom, top-1, -1):
                result.append(square_matrix[i][left])
            left += 1
        direction = (direction + 1) % 4

    if result:
        return result

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
