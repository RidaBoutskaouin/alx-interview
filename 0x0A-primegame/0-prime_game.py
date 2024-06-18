#!/usr/bin/python3
"""0. Prime Game Maria and Ben are playing a game."""


def isWinner(x, nums):
    """isWinner function to determine the winner of the game"""
    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [1 for _ in range(max(n + 1, 2))]
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    sieve = [i for i, n in enumerate(sieve) if n]
    sieve = sieve[1:]

    count = 0
    for i in nums:
        count += sum(1 for prime in sieve if prime <= i)
    if count % 2 == 0:
        return "Ben"
    return "Maria"

