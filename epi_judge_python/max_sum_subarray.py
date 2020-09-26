from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:

    if not A:
        return 0

    if len(A) == 2:
        maxElement = max(A)
        maxSum = max(sum(A), maxElement)

    currentSum = A[0]
    maxSum = A[0]

    for i in range(1, len(A)):
        currentSum = max(currentSum + A[i], A[i])
        maxSum = max(maxSum, currentSum)

    if maxSum > 0:
        return maxSum
    else:
        return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
