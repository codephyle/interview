"""
Given an array of positive numbers and a positive number 'k',
find the maximum sum of any contiguous subarray of size 'k'.
"""


def maxsum_subarr_k(arr, k):
    max_sum, run_sum = 0, 0
    start, i = 0, 0
    for i in range(0, len(arr)):
        run_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, run_sum)
            run_sum -= arr[start]
            start += 1
    return max_sum


maxsum_subarr_k([2, 1, 5, 1, 3, 2], 3)

"""
Given an array of positive numbers and a positive number 'S',
find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'.

Return 0 if no such subarray exists.
"""


def smallest_subarray_with_given_sum(arr, s):
    runsum = 0
    minlen = 0
    start = 0

    for i in range(len(arr)):
        runsum += arr[i]
        while runsum >= s:
            minlen = min(minlen, i - start + 1)
            runsum -= arr[start]
            start += 1

    return minlen
