#!/usr/bin/python3

def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    
    # Initialize DP array, where dp[i] is the minimum coins for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for 0 amount
    
    # Update the DP array for each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, return -1 (can't make the total)
    return dp[total] if dp[total] != float('inf') else -1

