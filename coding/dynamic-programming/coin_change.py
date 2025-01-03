# Coin Change

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Examples
# Input: coins = [1,2,5], amount = 11
# Output: 3

# Input: coins = [2], amount = 3
# Output: -1

# Input: coins = [1], amount = 0
# Output: 0

# https://leetcode.com/problems/coin-change/


def coinChange(coins, amount):
    need = [amount + 1] * (amount + 1)
    need[0] = 0

    for c in coins:
        for a in range(c, amount + 1):
            need[a] = min(need[a], need[a - c] + 1)

    return -1 if need[-1] > amount else need[-1]
