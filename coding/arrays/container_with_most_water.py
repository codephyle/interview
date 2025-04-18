# CONTAINER WITH MOST WATER

# You are given an integer array 'height' of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

def container_with_maxarea(height):
    left, right = 0, len(height) - 1
    water = 0
    while left < right:
        water = max(water, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return water
