# 907. Sum of Subarray Minimums

# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

# Example 1:
#   Input: arr = [3,1,2,4]
#   Output: 17
# Explanation:
#   Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
#   Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
#   Sum is 17.

# Example 2:

#   Input: arr = [11,81,94,43,3]
#   Output: 444

# https://leetcode.com/problems/sum-of-subarray-minimums/description/

def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    
    result = 0
    stack = []
    arr.append(0)  # Add a sentinel element to handle the last subarray

    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] > num:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result += arr[j] * (i - j) * (j - k)
            result %= MOD
        stack.append(i)

    return result
