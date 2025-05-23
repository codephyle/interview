# Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Examples

#     Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#     Output: [[1,6],[8,10],[15,18]]
#     Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

#     Input: intervals = [[1,4],[4,5]]
#     Output: [[1,5]]
#     Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
    res = []
    for i in sorted(intervals, key=lambda k: k.start):
        if res and i.start <= res[-1].end:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res.append(i)
    return res
