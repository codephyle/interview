"""
SECOND LARGEST IN AN ARRAY

Find the second largest element in an array
"""
def second_largest(nums):

    if len(nums) < 2:
        return None

    first, second = 0, 0
    for n in nums:
        if first < n:
            second = first
            first = n
        elif second < n < first:
            second = n

    return second

assert second_largest([1, 2, 3, 4]) == 3
