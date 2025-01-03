'''
NEXT PERMUTATION

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of 
arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their 
lexicographical order, then the next permutation of that array is the permutation that follows it in the 
sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order
(i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2]. Similarly, the next permutation of arr = [2,3,1] is [3,1,2]. While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.

tags: facebook, array, string, permutation

Approach:
 1. Find largest index 'k' such that nums[k] < nums[k+1]. 
    If not exists, that means the given permutation is the largest number. Return the same after reversing.
 2. Find largest index 'r' after index 'k' such that 'k' < 'r' and nums[r] > nums[k]
 3. Swap nums[k] and nums[l]
 4. Reverse subarray nums[k+1:]

 tags: facebook, array
'''
# https://leetcode.com/problems/next-permutation/

def reverse(a, i, j):
    while i <= j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

def nextPermutation(nums):

    n, k, r  = len(nums), float("-inf"), float("inf")

    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            k = i
            break

    if k < 0:
        reverse(nums, 0, n-1)
    else:
        for j in range(n-1, k, -1):
            if nums[j] > nums[k]:
                r = j
                break

        nums[k], nums[r] = nums[r], nums[k]
        reverse(nums, k+1, len(nums) - 1)

nextPermutation([2,3,6,5,4,1])