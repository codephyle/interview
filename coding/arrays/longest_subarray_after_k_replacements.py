"""
LONGEST SUBARRAY WITH ONES AFTER REPLACEMENT

Given an array containing 0s and 1s, if you are allowed to replace no more than 'k' 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.

Input: arr=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s
             having length 6.

Input: arr=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s
             having length 9.
"""


def length_of_longest_subarray(arr, k):
    i, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for j in range(len(arr)):
        if arr[j] == 1:
            max_ones_count += 1

        # Current window size is from window_start to window_end, overall we have a maximum of 1s
        # repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
        # and the remaining are 0s which should replace with 1s.
        # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' 0s
        if (j - i + 1 - max_ones_count) > k:
            if arr[i] == 1:
                max_ones_count -= 1
            i += 1

        max_length = max(max_length, j - i + 1)
    return max_length
