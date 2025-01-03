#
# Given an array, find the average of all subarrays of size 'K' in it.
#

def average_subarray_size_k(nums, k):

    runningSum = 0
    i, j = 0, k - 1
    first_sum = sum(nums[i:k])

    for i in range(0, len(nums) - k + 1)




print(average_subarray_size_k([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))


# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

def average_subarray_size_k(nums, k, threshold):
    running_sum = 0
    start = 0
    subarray_size = 0
    res = 0

    for i in range(len(nums)):
        running_sum += nums[i]
        if i >= k - 1:
            if (running_sum // k) >= threshold:
                res += 1
            running_sum -= nums[start]
            start += 1
            subarray_size += 1
    
    return res