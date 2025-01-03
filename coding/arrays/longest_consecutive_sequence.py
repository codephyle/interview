# LONGEST CONSECUTIVE SEQUENCE

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

#     Input: nums = [100,4,200,1,3,2]
#     Output: 4
#     Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#     Example 2:

#     Input: nums = [0,3,7,2,5,8,4,6,0,1]
#     Output: 9
# https://leetcode.com/problems/longest-consecutive-sequence/

def longest_consecutive_sequence(nums):
    nums = set(nums)
    best = 0
    for num in nums:
        # if num-1 is absent, then 'num' is a candidate for
        # starting a consecutive sequence!
        if num - 1 not in nums:
            y = num + 1
            while y in nums:
                y += 1
            best = max(best, y - num) # note this!
    return best


longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
