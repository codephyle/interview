"""
SMALLEST SUBARRAY WITH A GREATER SUM 

Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray 
whose sum is greater than or equal to 'S'. Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].

"""
def smallest_subarray_sum(s, arr):
    
  start, sum = 0, 0
  min_length = float("inf")

  for end in range(0, len(arr)):
    sum += arr[end] 
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while sum >= s:
      min_length = min(min_length, end - start + 1)
      sum -= arr[start]
      start += 1

  if min_length == float("inf"):
    return 0
  return min_length
