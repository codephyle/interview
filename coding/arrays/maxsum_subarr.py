#
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Note: A subarray is a contiguous part of an array.
#

def maxsum_subarray(nums):
    if not nums:
        return 0

    maxsum = nums[0]
    currsum = 0
    for num in nums:
        if currsum < 0:
            currsum = 0
        currsum += num
        maxsum = max(maxsum, currsum)
    return maxsum


# aha!
# can find second max etc.,
def f(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    print(nums)
    return max(nums)


f([-2, 1, -3, 4, -1, 2, 1, -5, 4])
maxsum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
