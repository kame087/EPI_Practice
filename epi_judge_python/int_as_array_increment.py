from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    """
    HIGH LEVEL:
    SANITY CHECK:
    -Check if list is empty:
        return empty array

    -ADD 1 to the very element in the array
    -Traverse backwards up to second element in array (len(A) - 1, 0, -1)
        check if current position is not equal to 10 is TRUE:
            -break
        otherwise:
            set current position to 0
            add 1 to next element in traversal (i.e.if index = 4, add 1 to element @index 3)

    -Take into account if the first digit ends up being 10 after iterating:
        set A[0] = 1
        append a 0 to end of array
    return array

    :param A:
    :return A:
    """
    if len(A) == 0:
        return []

    A[-1] += 1
    for i in range(len(A) - 1, 0, -1):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
