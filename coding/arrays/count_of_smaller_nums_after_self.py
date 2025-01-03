"""
COUNT OF SMALLER NUMBERS AFTER SELF

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements 
to the right of nums[i]

Example:

    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]

    Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.

    Input: nums = [-1]
    Output: [0]

    Input: nums = [-1,-1]
    Output: [0,0]

"""
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/


# O(n2)
def smallers(nums):
    counts = []
    for i in range(len(nums)):
        n, cnt = nums[i], 0
        for j in range(i + 1, len(nums)):
            if nums[j] < n:
                cnt += 1
        counts += (cnt,)
    return counts


smallers([5, 2, 6, 1])

# Optimal O(n logn) using Segment/Fenwick Tree
