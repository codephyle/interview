# SHORTEST UNSORTED CONTINUOUS SUBARRAY

# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0

# From the beginning and end of the array, find the first elements that are out of the sorting order. The two elements will be our candidate subarray. Find the maximum and minimum of this subarray. Extend the subarray from beginning to include any number which is bigger than the minimum of the subarray. Similarly, extend the subarray from the end to include any number which is smaller than the maximum of the subarray.


def findUnsortedSubarray(nums):
    n = len(nums)
    start, end = n - 1, 0

    # Find the first element out of sorting order from the beginning
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            start = i
            break

    # Find the first element out of sorting order from the end
    for i in range(n - 1, 0, -1):
        if nums[i] < nums[i - 1]:
            end = i
            break

    # If the array is already sorted
    if start == n - 1 and end == 0:
        return 0

    # Find the minimum and maximum elements in the subarray
    min_val = min(nums[start : end + 1])
    max_val = max(nums[start : end + 1])

    # Extend the subarray from the beginning
    while start > 0 and nums[start - 1] > min_val:
        start -= 1

    # Extend the subarray from the end
    while end < n - 1 and nums[end + 1] < max_val:
        end += 1

    return end - start + 1


nums = [2, 6, 4, 8, 10, 9, 15]
print(findUnsortedSubarray(nums))
