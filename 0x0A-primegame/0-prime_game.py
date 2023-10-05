#!/usr/bin/python3
"""Prime game module."""


def isWinner(rounds, nums):
    """Determines the winner of a prime game session with `rounds` rounds.

    Args:
        rounds (int): The number of rounds in the game.
        nums (list): A list of integers representing the limit for
        prime generation in each round.

    Returns:
        str or None: The name of the winner ('Maria' or 'Ben'),
        or None if it's a tie.
    """
    if rounds < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0

    # Generate primes with a limit of the maximum number in nums
    max_num = max(nums)
    primes = [True for _ in range(1, max_num + 1)]
    primes[0] = False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i - 1]:
            for j in range(i * i, max_num + 1, i):
                primes[j - 1] = False

    # Count the number of primes less than or equal to n in nums for each round
    for _ in range(rounds):
        n = nums.pop(0)
        primes_count = sum(1 for i in range(n) if primes[i])
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1

    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"
