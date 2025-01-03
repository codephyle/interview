"""
Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
    
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
"""
# https://leetcode.com/problems/kth-largest-element-in-an-array/
from collections import heapq


def kth(arr, k):
    return sorted(arr)[-k]


def kth(arr, k):
    return heapq.nlargest(k, arr)[-1]


import random

def partition(nums, left, right):
    
    pivot_index = random.randint(left, right)
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

    i = left
    for j in range(left, right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i

def quickselect(nums, left, right, k):
    if left == right:
        return nums[left]
    pivot_index = partition(nums, left, right)
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return quickselect(nums, left, pivot_index - 1, k)
    else:
        return quickselect(nums, pivot_index + 1, right, k)

def findKthLargest(nums, k):
    return quickselect(nums, 0, len(nums) - 1, len(nums) - k)


### heap

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Convert the list to a min-heap
    heap = nums[:k]
    heapq.heapify(heap)
    
    # Iterate through the remaining elements in nums
    for num in nums[k:]:
        # Push the current element onto the heap
        heapq.heappush(heap, num)
        # If the heap size exceeds k, pop the smallest element
        if len(heap) > k:
            heapq.heappop(heap)
    
    # The kth largest element is the root of the heap
    return heap[0]



###
import statistics

def partition(nums, left, right, pivot_index):
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left
    for i in range(left, right):
        if nums[i] < pivot_value:
            nums[i], nums[store_index] = nums[store_index], nums[i]
            store_index += 1
    nums[right], nums[store_index] = nums[store_index], nums[right]
    return store_index

def select(nums, left, right, k):
    if left == right:
        return nums[left]
    
    # Divide the array into sublists of size 5 and find median of each sublist
    medians = []
    for i in range(left, right + 1, 5):
        sub_right = min(i + 4, right)
        median = statistics.median(nums[i:sub_right + 1])
        medians.append(median)
    
    # Find the median of medians
    median_of_medians = select(medians, 0, len(medians) - 1, len(medians) // 2)
    
    # Partition the array around the median of medians
    pivot_index = nums.index(median_of_medians)
    pivot_index = partition(nums, left, right, pivot_index)
    
    # Recurse on the appropriate sublist
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return select(nums, left, pivot_index - 1, k)
    else:
        return select(nums, pivot_index + 1, right, k)

def findKthLargest(nums, k):
    return select(nums, 0, len(nums) - 1, len(nums) - k)

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Output should be 5

