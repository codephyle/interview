"""
Given an array of intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove
to make the rest of the intervals non-overlapping.
"""


def erase_overlaps(intervals):
    end = float("-inf")
    erased = 0
    for i in sorted(intervals, key=lambda k: k.end):
        if i.start > end:
            end = i.end
        else:
            erased += 1
    return erased
