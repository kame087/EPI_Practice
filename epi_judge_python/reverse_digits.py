from test_framework import generic_test


def reverse(x: int) -> int:
    """
        Brute force:
            Convert the number into a string, and then convert it into a list
            swap values to reverse the list
            then return an int type cast of the list that's converted into a string.

        Time: O(n^2), n = # digits in x, to convert into string and then into a list.
        Space: O(n), to hold the x as a list of chars

        Optimized:
            By using math, we can avoid using strings by using % 10 to capture the first digit
            and adding it to result * 10, you multiply result * 10 first, because prior to adding the % 10,
            we need to shift the existing result value to it's appropriate location (tens place, thousands place, etc).
            update x by dividing by 10 to remove the first digit

            i.e. 1234:
                result = 0
                1234 % 10 = 4
                result = 0 * 10 + (1234 % 10) # result = 4
                1234 // 10 = 123
                .
                .
                123 % 10 = 3
                result = 4 * 10 + (123%10) # result = 43
                123 //= 10 = 12
                .
                .
                12 % 10 = 2
                result = 43 * 10 + (12 % 10) # result = 432
                12 //= 10 = 1
                .
                .
                1 % 10 =1
                result = 432 *10 + (1 %10) # result = 4321
                1 // 10 = 0
                .
                .
                x = 0...BREAK OUT OF LOOP

    :param x:
    :return:
    """
    result = 0
    x_num = abs(x)
    while x_num:
        result = result * 10 + x_num % 10
        x_num //= 10

    return -result if x < 0 else result





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
