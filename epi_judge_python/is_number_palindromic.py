from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    """
        HIGH LEVEL:
            First do sanity checks:
                * Check if x is negative:
                    return False

            You essentially want to reverse x
            * First save x to a variable, because you don't want to manipulate the original input, since you're going to compare it at the end.
            * Have a x_reversed variable that will hold the reverse of x
            * To reverse x:
                * isolate the right most digit by using mod 10
                * shift existing x_reversed to the next place value by multiplying it by 10 and then add the right most digit of x
                * eliminate the right most digit of x by dividing x by 10

            return x == x_reversed # True is they're equal, False if not.

        Time Complexity: O(n), n = number of digits in x
        Space Complexity: O(1)


    :param x:
    :return:
    """
    if x < 0:
        return False

    x_manip = x
    x_reversed = 0
    while x_manip:
        x_reversed = x_reversed * 10 + x_manip % 10
        x_manip //= 10


    return x == x_reversed



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
