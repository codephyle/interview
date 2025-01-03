# NEXT INTERVAL

# Given an array of intervals, find the next interval of each interval. In a list of intervals, for an interval i its next interval j will have the smallest 'start' greater than or equal to the 'end' of i.

# Write a function to return an array containing indices of the next interval of each input interval. If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

# Input: Intervals [[2,3], [3,4], [5,6]]
# Output: [1, 2, -1]
# Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, 
# the next interval of [3,4] is [5,6] having index ‘2’. There is no next interval for [5,6] hence we have ‘-1’.

# Input: Intervals [[3,4], [1,5], [4,6]]
# Output: [2, -1, -1]
# Explanation: The next interval of [3,4] is [4,6] which has index ‘2’. 
# There is no next interval for [1,5] and [4,6].

# https://leetcode.com/problems/find-right-interval/solution/

def find_next_interval(intervals):
    n = len(intervals)
    result = [-1] * n
    starts = []
    for i in range(n):
        starts.append((intervals[i][0], i))
    starts.sort()
    for i in range(n):
        end = intervals[i][1]
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if starts[mid][0] >= end:
                result[i] = starts[mid][1]
                right = mid - 1
            else:
                left = mid + 1
    return result

intervals = [[2,3], [3,4], [5,6]]
print(find_next_interval(intervals))

intervals = [[3,4], [1,5], [4,6]]
print(find_next_interval(intervals))