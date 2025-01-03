# 1963. Minimum Number of Swaps to Make the String Balanced

# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

# A string is called balanced if and only if:

# Return the minimum number of swaps to make s balanced.

# Example 1:

#     Input: s = "][]["
#     Output: 1
#     Explanation: You can make the string balanced by swapping index 0 with index 3.
#     The resulting string is "[[]]".

def minSwaps(s):
    close, maxClose = 0, 0
    for c in s:
        if c == ']':
            close += 1
        else:
            close -= 1
        maxClose = max(maxClose, close)
    return (maxClose + 1 ) // 2

def minSwaps(s):
    imbalance = 0

    for c in s:
        if c == "[":
            imbalance += 1
        elif imbalance > 0:
            imbalance  -= 1
    return (imbalance + 1) / 2