from test_framework import generic_test


def parity(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1

    if num_bits % 2 != 0:
        return 1
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
