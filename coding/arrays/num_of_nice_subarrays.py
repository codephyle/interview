# 1248. Count Number of Nice Subarrays

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Input: nums = [2,4,6], k = 1
# Output: 0


# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
def num_of_nice_subarrays(nums, k):
    count = 0
    odd_count = 0
    prefix_sum = [0] * (len(nums) + 1)
    prefix_sum[0] = 1

    for num in nums:
        if num % 2 == 1:
            odd_count += 1
        if odd_count >= k:
            count += prefix_sum[odd_count - k]
        prefix_sum[odd_count] += 1

    return count


def numberOfSubarrays(self, nums, k):
    i = count = res = 0
    for j in range(len(nums)):
        if nums[j] & 1:
            k -= 1
            count = 0
        while k == 0:
            k += nums[i] & 1
            i += 1
            count += 1
        res += count
    return res
