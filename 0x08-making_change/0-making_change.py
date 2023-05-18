#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the fewest number of coins for each total
    dp = [float('inf')] * (total + 1)

    # 0 coins are needed to make a total of 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the dp values for each possible total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If it is not possible to make the total, return -1
    if dp[total] == float('inf'):
        return -1

    # Return the fewest number of coins needed for the total
    return dp[total]
