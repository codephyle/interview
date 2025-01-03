"""
SMALLEST DIFFERENCE

Write a function that takes two non-empty array of integers, find the pair of numbers (one from each array) whose absolute difference is 
closest to zero, and return an array containing these two numbers, with the number from the first array in the first position.

Note: abs_diff(-5, 5) = 10

Assume there will only be one pair of numbers with the smallest difference.

source: algoexpert.io
"""
def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    i, j = 0, 0
    curr, smallest = float("inf"), float("inf")
    ans = []

    while i < len(arr1) and j < len(arr2):
        f, s = arr1[i], arr2[j]
        if f < s:
            curr = s - f
            i += 1
        elif f > s:
            curr = f - s
            j += 1
        else:
            return [f, s]

        if smallest > curr:
            smallest = curr
            ans = [f, s]

    return ans

smallestDifference([-1, 5, 10, 20, 28, 3],  [26, 134, 135, 15, 17]) == [28, 26]
smallestDifference( [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]) == [530, 530]