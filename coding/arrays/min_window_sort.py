"""
MINIMUM WINDOW SORT

Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""
#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# easy (nlogn) solution
def min_window_sort(nums):
    i, j = 0, len(nums) - 1
    sorted_nums = sorted(nums)

    if sorted_nums == nums:
        return 0

    while sorted_nums[i] == nums[i]:
        i += 1

    while sorted_nums[j] == nums[j]:
        j -= 1

    return j - i + 1


def min_window_sort_optimal(nums):
    l, r = 0, len(nums) - 1

    while l < r and nums[l] <= nums[l+1]:
        l += 1
    
    if l == r:
        return 0

    while r > 0 and nums[r-1] <= nums[r]:
        r -= 1

    minimum, maximum = min(nums[l:r+1]), max(nums[l:r+1])

    while minimum >= nums[l]:
        l -= 1

    while maximum <= nums[r]:
        r += 1

    return r - l + 1

min_window_sort([2, 6, 4, 8, 10, 9, 15])
min_window_sort_optimal([2, 6, 4, 8, 10, 9, 15])
