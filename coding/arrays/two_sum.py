# Two Sum https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):

    seen = {}
    for i, n in enumerate(nums):
        remainder = target - n
        if remainder in seen:
            return [i, seen[remainder]]
        seen[n] = i


two_sum([2, 7, 11, 15], 17)  # [0,1]
two_sum([3, 3], 6)  # [0,1]


# 3Sum 

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Input: nums = [0]
# Output: []
# https://leetcode.com/problems/3sum/

def three_sum(nums, target):
    result = []
    nums.sort()
    n = len(nums)
    for i in range(n - 2):

        # avoid dups
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return result

def three_sum_closest(nums, target):
    
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum
            if curr_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum

def three_sum_smaller(nums, target):
    nums.sort()
    n = len(nums)
    count = 0
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count

def four_sum(nums, target):
    result = []
    nums.sort()
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if curr_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return result
