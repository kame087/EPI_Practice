from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    """
        HIGH LEVEL:
            First do sanity checks:
                If array is empty: return 0

                If there's only 2 elements in the array: return the max between the sum(A) and maxElement(A)

            What it boils down to is you're going to treat this problem like a sliding window.
            You're either going to expand your sum, or start over:
            initialize current_running_sum = A[0]
            max_sum = A[0]
            At every iteration of the array i=1 -> len(A)-1:
                * You're essentially choosing the max between your current_running_sum + current_number OR the current_number: A[i] # to simulate either expanding the window, or starting over
                * then update the max_sum by choosing the max between max_sum, current_running_sum


            return max_sum if max_sum > 0 else return 0

        Time Complexity: O(n), n = len(A)
        Space Complexity: O(1)


    :param A:
    :return:
    """

    if not A:
        return 0

    if len(A) == 2:
        maxSum = max(sum(A), max(A))

    currentSum = A[0]
    maxSum = A[0]

    for i in range(1, len(A)):
        currentSum = max(currentSum + A[i], A[i])
        maxSum = max(maxSum, currentSum)

    return maxSum if maxSum > 0 else 0




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
