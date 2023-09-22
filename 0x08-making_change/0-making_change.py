#!/usr/bin/python3
"""
Change making module.
"""


def makeChange(coins: int, total: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given
    amount (total_amount) when given a pile of coins of different
      values (coins).
    :param coins: List of coin denominations (e.g., [1, 5, 10, 25] for cents)
    :param total_amount: The target amount to make change for
    :return: The minimum number of coins needed, or -1 if change cannot be made
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            coin_count += 1

    if total == 0:
        return coin_count
    else:
        return -1
