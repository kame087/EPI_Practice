from test_framework import generic_test


def power(x: float, y: int) -> float:
    """
    This is a brute force solution:
        basically use looping to calculate the power of a base.
        There is a quicker computation using bits. But I need to look into it.
        Time: O(2^n), y = the power, and it takes y-1 multiplications
        Space: O(1)

    Optimized solution:
        The approach is that you're trying to reduce the amount of multiplications needed
        to get to the product. One example would be 1.1^21 = 1.1 * 1.1^20, we could treat
        it as 1.1 * 1.1^2(10 times) which will give us 11 multiplications instead of 21.

        One way to do that is to check if the most significant bit of y is 1:
            you multiply the result * base (which at every iteration, the base is squaring itself.
            but you only multiply the new base with the result whenever the least significant bit of y is 1.

        Time: O(n), number of multiplications is at most twice the index of y's most significant bit.
        Space: O(1)

    :param x:
    :param y:
    :return:
    """
    product, base, power = 1.0, x, y

    if y < 0:
        base = 1.0/x
        power = -power

    while power: # while power is greater than 0
        if power & 1: # if the least significant bit is 1
            product *= base # update the result by multiplying it with base
        base = base * base # keep exponentially updating base by squaring it's already updated value
        power = power >> 1 # right shift y, to check its next bit in the next iteration.

    return product


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
