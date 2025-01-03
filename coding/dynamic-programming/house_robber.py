"""
House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 2:

    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.
"""


# https://leetcode.com/problems/house-robber/
def rob(nums):
    if not nums:
        return 0

    n = len(nums)
    if n == 1:
        return nums[0]

    prev_house = nums[0]
    curr_house = max(nums[0], nums[1])

    for i in range(2, n):
        # At each house, decide whether to rob it or skip it
        # If robbing the current house, add the maximum amount robbed up to the previous non-adjacent house
        # If skipping the current house, take the maximum amount robbed up to the previous house
        temp = curr_house
        curr_house = max(nums[i] + prev_house, curr_house)
        prev_house = temp

    # Return the maximum amount robbed up to the last house
    return curr_house


# Test cases
print(rob([1, 2, 3, 1]))  # Output: 4
print(rob([2, 7, 9, 3, 1]))  # Output: 12
