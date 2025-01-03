"""
MAJORITY ELEMENT

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Examples
    Input: nums = [3,2,3]
    Output: 3

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""

# https://leetcode.com/problems/majority-element/
# See, https://leetcode.com/problems/majority-element-ii/discuss/63502/6-lines-general-case-O(N)-time-and-O(k)-space

import collections


def majority(nums):
    n = len(nums)
    threshold = n // 2

    count = collections.Counter(nums)
    for num, freq in count.items():
        if freq > threshold:
            return num

    return None


# Boyer-Moore Voting Algorithm
def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


majority([2, 2, 1, 1, 1, 2, 2])


# majority II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
def majority_elements(nums):
    n = len(nums)
    threshold = n // 3
    count = collections.Counter(nums)
    result = []
    for num, freq in count.items():
        if freq > threshold:
            result.append(num)
    return result


majority_elements([2, 2, 1, 1, 1, 2, 2])


majority_element([2, 2, 1, 1, 1, 2, 2])
