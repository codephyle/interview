# TRAPPING RAIN WATER

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

#  https://leetcode.com/problems/trapping-rain-water/

# Keep track of the already safe level and the total water so far.
# In each step, process and discard the lower one of the leftmost or rightmost elevation.
#
def trap(height):

    l, r = 0, len(height) - 1
    level, water = 0, 0

    while l < r:
        if height[l] < height[r]:
            lower = height[l]
            l += 1
        else:
            lower = height[r]
            r -= 1
        level = max(level, lower)
        water += level - lower

    return water


trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
trap([4, 2, 0, 3, 2, 5]) == 9
