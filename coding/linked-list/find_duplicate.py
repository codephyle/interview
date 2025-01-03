"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2] 15 12 3
Output: 2

Example 2:
Input: nums = [3,3,3,3,3]
Output: 3
 
"""
def findDuplicate(nums):
    # Phase 1: Detect the intersection point of the two pointers
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: Find the entrance to the cycle
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

# Example usage:
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2