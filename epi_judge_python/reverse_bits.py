from test_framework import generic_test
import math

def reverse_bits(x: int) -> int:
    """
        HIGH LEVEL:
            I think this is a brute force, and I have to read further to see how the book explains an optimized version

            I know that the length of the integer is 64 bits.
            My intuition is to create a list that will store the values of each bit in reverse order already
            Since every time we check for the value of the least significant bit, that value will be added
            first to the list. By default our list will have the bits in reverse order.

            After you add the value of each bit to list
            Iterate through the list, and OR it with your result value which is initialized to 0.
            As you iterate i: 0-> len(list):
                right shift your result by 1, to make room for the next bit
                OR the result value with the value at index i to add value @i to the result at current position

            return result

            at every iteration while length > 0:
                use AND bitwise operator to get value of current LSB
                add value to list
                RIGHT SHIFT num by 1 to check next LSB
                decrement length

            your list will now have the bits in reverse order

            * # next is to convert your list into an integer value "result"
            * at every iteration of your list:
                LEFT SHIFT result by 1 to prepare a spot for list[i]
                result = result OR with list[i] to add bit value to position that you prepared with the LEFT SHIFT

            return result

            Time: O(1), since the length is always 64 bits, but you can argue it's O(n), n = length of integer.
            Space: O(1), since the length of the list is always 64, but you can argue it's O(n), n = length of integer


    :param x:
    :return:
    """
    bit_length = 64
    num_list = []

    while bit_length > 0:
        val = x & 1
        num_list.append(val)
        x >>= 1
        bit_length -= 1

    result = 0
    for i in range(len(num_list)):
        result <<= 1
        result = result | num_list[i]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
