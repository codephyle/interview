"""
DEGREE OF AN ARRAY

Given a non-empty array of non-negative integers nums, the degree of this array is defined 
as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.


Examples

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: The input array has a degree of 2 because both elements 1 and 2 appear twice.
             Of the subarrays that have the same degree:
                 [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
             The shortest length is 2. So return 2.

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: The degree is 3 because the element 2 is repeated 3 times.
             So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 
Constraints:

    nums.length will be between 1 and 50,000.
    nums[i] will be an integer between 0 and 49,999.

"""
# https://leetcode.com/problems/degree-of-an-array/
from collections import defaultdict

def degreeOfArray(arr):
    left, right, count = {}, {}, defaultdict(int)
    for i, n in enumerate(arr):
        if n not in count: 
            left[n] = i
        right[n] = i
        count[n] += 1

    min_len = len(arr)
    degree = max(count.values())

    for n in count.keys():
        if count[n] == degree:
            min_len = min(min_len, right[n] - left[n] + 1)
    
    return min_len

degreeOfArray([1, 2, 1, 3, 2, 1])
    