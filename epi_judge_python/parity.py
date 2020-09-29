from test_framework import generic_test


def parity(x: int) -> int:
    bit_count = 0

    while x:
        bit_count += x & 1
        x >>= 1

    if bit_count % 2 == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
