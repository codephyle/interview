# MERGE SORTED ARRAY

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# EXAMPLES

#     Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#     Output: [1,2,2,3,5,6]
#     Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
   

#     Input: nums1 = [1], m = 1, nums2 = [], n = 0
#     Output: [1]
#     Explanation: The arrays we are merging are [1] and [].

#     Input: nums1 = [0], m = 0, nums2 = [1], n = 1
#     Output: [1]
#     Explanation: The arrays we are merging are [] and [1].

# tags: facebook, array, sorting, easy

# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/309/
def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    # copy the remaining elements
    if n > 0:
        nums1[:n] = nums2[:n]

    
nums1,m = [1,2,7,0,0,0],3 
nums2,n = [2,5,6], 3
merge(nums1, m, nums2, n)
print(nums1)