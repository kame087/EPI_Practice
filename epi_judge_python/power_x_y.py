from test_framework import generic_test


def power(x: float, y: int) -> float:
    """
    This is a brute force solution:
        basically use looping to calculate the power of a base.
        There is a quicker computation using bits. But I need to look into it.
        Time: O(2^n), y is the power, it takes y-1 multiplications
        Space: O(1)

    :param x:
    :param y:
    :return:
    """
    product = 1.0
    base = x
    power = y
    if y < 0:
        base = 1/x
        power = -power

    while power:
        product *= base
        power -= 1

    return product


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
