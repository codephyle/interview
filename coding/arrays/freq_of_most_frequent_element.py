# 1838. Frequency of the Most Frequent Element

# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

# Examples:

# Input: nums = [1,2,4], k = 5   Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4]. 4 has a frequency of 3.

# Input: nums = [1,4,8,13], k = 5  Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

# Input: nums = [3,9,6], k = 2
# Output: 1

def max_frequency(nums, k):
    nums.sort() 
    n = len(nums)
    
    left, right = 0, 0 
    max_freq = 0  
    curr_sum = 0 

    while right < n:
        curr_sum += nums[right]  # Add the current element to the sum
        # Calculate the number of operations needed to make all elements in the window equal
        operations = (right - left + 1) * nums[right] - curr_sum

        if operations <= k:  # If the number of operations is less than or equal to k
            max_freq = max(max_freq, right - left + 1)  # Update the maximum frequency
        else:
            curr_sum -= nums[left]  # Subtract the leftmost element from the sum
            left += 1  # Move the left pointer to the right

        right += 1  # Move the right pointer to the right

    return max_freq
