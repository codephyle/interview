"""
SUBARRAYS WITH PRODUCT LESS THAN A TARGET

Given an array with positive numbers and a positive target number, 
find all of its contiguous subarrays whose product is less than the target number.

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.

"""
from collections import deque


def subarrays_product_ceil(nums, t):
    if not nums:
        return nums

    product, j = 1, 0
    ans = []
    cnt = 0  # to only count, a variant of the problem
    for i in range(len(nums)):
        product *= nums[i]
        while product >= t and j < len(nums):
            product //= nums[j]
            j += 1

        # all subarrays within i and j has product less than t
        temp = deque()
        print(i, j)
        for k in range(i, j - 1, -1):
            temp.append(nums[k])
            ans.append(list(temp))
        print(ans)
        cnt += i - j + 1
    return ans


subarrays_product_ceil([2, 5, 3, 10], 30)
