# FIND MINIMUM IN ROTATED SORTED ARRAY

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
#     Input: nums = [3,4,5,1,2], Output: 1
#     Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
#     Input: nums = [4,5,6,7,0,1,2], Output: 0
#     Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

def mini(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    return nums[l]


# naive
def minimum(nums):
    smallest = nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            smallest = nums[i]
            break

    return smallest


mini([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
