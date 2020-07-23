from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    max_profit = float("-inf")
    lowest = prices[0]

    for i in range(1, len(prices)):
        lowest = min(lowest, prices[i])
        max_profit = max(max_profit, prices[i] - lowest)

    if max_profit != float("-inf"):
        return max_profit
    return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
