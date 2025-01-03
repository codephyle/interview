"""
SMALLEST RANGE COVERING ELEMENTS FROM K LISTS

You have k lists of sorted integers in non-decreasing order. 
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Input: nums = [ [4, 10, 15, 24, 26 ], 
                [0,  9, 12, 20 ],
                [5, 18, 22, 30 ]]
Output: [20,24]
Explanation: 
    List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
    List 2: [0, 9, 12, 20], 20 is in range [20,24].
    List 3: [5, 18, 22, 30], 22 is in range [20,24].

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

"""
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
import heapq
import math


def smallest_range(a):
    pq = [(row[0], list, 0) for list, row in enumerate(a)]  # (value, list, index)
    heapq.heapify(pq)

    ans = -math.inf, math.inf
    right = max(row[0] for row in a)
    while pq:
        left, list, i = heapq.heappop(pq)  # (value, list, index)
        if right - left < ans[1] - ans[0]:
            ans = left, right
        if i == len(a[list]) - 1:  # end of list with smallest element seen so far
            return ans
        v = a[list][i + 1]
        right = max(right, v)
        heapq.heappush(pq, (v, list, i + 1))
        print(pq)


smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
