# REMOVE DUPLICATES FROM SORTED ARRAY

# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Return 'k' after placing the final result in the first k slots of nums.

# Examples:

#     Input: nums = [1,1,2]
#     Output: 2, nums = [1,2,_]

#     Input: nums = [0,0,1,1,1,2,2,3,3,4]
#     Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# tags: facebook, array

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):

    if not nums: 
        return 0
    
    n = len(nums)
    if n < 2:
        return n

    p = 0
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            p += 1
            nums[p] = nums[i]

    return p + 1

removeDuplicates([0,0,1,1,1,2,2,3,3,4])
removeDuplicates([1,1,1,2,2])

'''
Follow up:

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place 
such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Examples:

    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]

    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
'''

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
def removeDuplicates2(nums):
    if len(nums) < 3:
        return 
    
    processed = 0
    for i in (1, range(len(nums))):

# TODO 