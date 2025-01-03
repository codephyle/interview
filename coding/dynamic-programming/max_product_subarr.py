"""
MAXIMUM PRODUCT SUBARRAY

Given an integer array nums, find a contiguous non-empty subarray within the array 
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


# https://leetcode.com/problems/maximum-product-subarray/
def max_product_subarray(nums):

    if not nums:
        return 0

    reversed_nums = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        reversed_nums[i] *= reversed_nums[i - 1] or 1

    return max(nums + reversed_nums)


def max_product_subarray2(nums):

    max_positive, max_negative, max_product = 1, 1, float("-inf")
    for num in nums:
        temp_positive = max(num, num * max_positive, num * max_negative)
        temp_negative = min(num, num * max_negative, num * max_positive)
        max_positive, max_negative = temp_positive, temp_negative
        max_product = max(max_positive, max_negative, max_product)
    return max_product


max(max_product_subarray([2, 3, -2, 4]))


def subsets(nums):
    result = [[]]
    for n in nums:
        for i in range(len(result)):
            result.append(result[i] + [n])
    return result


subsets([2, 3, -2, 4])
