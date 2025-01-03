# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer x, write a function to search x in nums. If x exists, then return its index. Otherwise, return -1.


# You must write an algorithm with O(log n) runtime complexity.
def binary_search(nums, x):

    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if x < nums[mid]: 
            hi = mid - 1
        elif x > nums[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

def bisect_right(nums, x):

    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if x < nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo
        