#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    For each i > 1, we can calculate dp[i] by iterating over all j < i
    and checking if we can form i by copying dp[j] characters
    and pasting them i-j times.
    If this is possible,
    then we can update dp[i] to dp[j] + i/j.
    We take the minimum value of all such dp[j] and update dp[i] to that value.
    """
    dp = [float('inf')] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i//j)
    if dp[n] == float('inf'):
        return 0
    else:
        return dp[n]
