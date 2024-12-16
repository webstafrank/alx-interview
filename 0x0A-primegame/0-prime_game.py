#!/usr/bin/python3
"""
Prime Game Module
"""

def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the maximum number for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
        None: If the result is a tie.
    """
    if not nums or x < 1:
        return None

    # Step 1: Compute all primes up to the maximum value in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Step 2: Simulate the game for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Step 3: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(limit):
    """
    Computes the number of primes up to a given limit using the Sieve of Eratosthenes.

    Args:
        limit (int): The upper limit to compute primes.

    Returns:
        list: A list where the value at index i represents the count of primes <= i.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    # Create a cumulative prime count array
    prime_count = [0] * (limit + 1)
    count = 0
    for i in range(limit + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    return prime_count

