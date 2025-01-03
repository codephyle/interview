# SLIDING WINDOW MAXIMUM

# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right.

# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example

#     Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#     Output: [3,3,5,5,6,7]

#     Explanation:
#     Window position                Max
#     ---------------               -----
#     [1  3  -1] -3  5  3  6  7       3
#     1 [3  -1  -3]  5  3  6  7       3
#     1  3 [-1  -3  5]  3  6  7       5
#     1  3  -1 [-3  5  3]  6  7       5
#     1  3  -1  -3 [5  3  6]  7       6
#     1  3  -1  -3  5 [3  6  7]      7

# https://leetcode.com/problems/sliding-window-maximum/

"""
Solution

Keep indexes of good candidates in deque 'd'. 
The indexes in 'd' are from the current window, they're increasing, 
and their corresponding nums are decreasing. 
Then the first deque element is the index of the largest window value.

For each index i:
    1. Pop (from the end) indexes of smaller elements (they'll be useless).
    2. Append the current index.
    3. Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
    4. If our window has reached size k, append the current window maximum to the output.

"""
from collections import deque


def sliding_window_max(nums, k):

    queue = deque()
    out = []
    for i, n in enumerate(nums):
        # remove all the smaller elements in the queue from right
        while queue and nums[queue[-1]] < n:
            queue.pop()

        queue.append(i)

        if queue[0] == i - k:  # d[0] falls out of the window
            queue.popleft()

        # append to result only after the processing the first 'k' elements
        if i >= k - 1:
            out.append(nums[queue[0]])

    return out


sliding_window_max(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
