# DUTCH NATIONAL FLAG PROBLEM

# Given an array containing 0s, 1s and 2s, sort the array in-place. 
# You should treat numbers of the array as objects, hence, 
# we can't count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; 
# and since our input array also consists of three different numbers that is 
# why it is called Dutch "National Flag problem".

# Input: [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]

# Input: [2, 2, 0, 1, 2, 0]
# Output: [0, 0, 1, 2, 2, 2]

def dutch_flag_sort(nums):
    
    l, r = 0, len(nums) - 1
    i = 0

    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
            i += 1
        elif nums[i] == 1:
            l += 1
        else:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
    
    return nums
