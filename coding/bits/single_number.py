"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    Input: nums = [2,2,1] Output: 1

Example 2:
    Input: nums = [4,1,2,1,2] Output: 4

Example 3:
    Input: nums = [1] Output: 1

"""

def singleNumber(nums):
    x = 0
    for n in nums:
        x = x ^ n
    return x

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(self, nums: List[int]) -> int:

    # Initialize seen_once and seen_twice to 0
    seen_once = seen_twice = 0

    # Iterate through nums
    for num in nums:
        # Update using derived equations
        seen_once = (seen_once ^ num) & (~seen_twice)
        seen_twice = (seen_twice ^ num) & (~seen_once)

    # Return integer which appears exactly once
    return seen_once


# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

def singleNumber(self, nums: int) -> List[int]:
    # difference between two numbers (x and y) which were seen only once
    bitmask = 0
    for num in nums:
        bitmask ^= num
    
    # rightmost 1-bit diff between x and y
    diff = bitmask & (-bitmask)
    
    x = 0
    for num in nums:
        # bitmask which will contain only x
        if num & diff:
            x ^= num
    
    return [x, bitmask^x]