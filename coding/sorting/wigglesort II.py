"""
WIGGLE SORT II

Given an integer array nums, reorder it
such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

"""
# https://leetcode.com/problems/wiggle-sort-ii/
def wiggle_sort(nums):
    """
    Example nums = [1,2,...,7]      Example nums = [1,2,...,8]

    Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
    Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
    --------------------------      --------------------------
    Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5
    """
    nums.sort()
    half = len(nums[::2])
    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


assert wiggle_sort([1, 5, 1, 1, 6, 4]) == [1, 6, 1, 5, 1, 4] or wiggle_sort(
    [1, 5, 1, 1, 6, 4]
) == [1, 4, 1, 5, 1, 6]

assert wiggle_sort([1, 3, 2, 2, 3, 1]) == [2, 3, 1, 3, 1, 2]

# https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing
