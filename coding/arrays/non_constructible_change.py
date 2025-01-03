"""
Given an array of positive integers representing the values of coins in your possession, 
write a function that returns the minimum amount of change that you connot create.

The given coins are not unique.

source: algoexpert.io
"""
# little math involved. +1 check needs attention
def nonContructibleChange(coins):
    coins.sort()
    curr = 0

    for coin in coins:
        if coin > curr + 1:
            return curr + 1
        curr += coin
    
    return curr + 1

assert nonContructibleChange([5, 7, 1, 1, 2, 3, 22]) == 20
