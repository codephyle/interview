"""
SUBSEGMENT SORT

An array of n integers, arr[n] can be partitioned into any number of contiguous subsegments. Every element must present in exactly 1 partition.
After partitioning, and without changing the order of partitions, sort each partition in non-descending order. 
Concatenate the sorted partitions and compare the resulting array to the original array, sorted non-descending. If the two match, the set of partitions is valid.

Find the maximum number of contiguous subsegments in which the array arr can be partitioned such that the set of partitions is valid.

Example
n = 6
arr = [2, 5, 1, 9, 7, 6]

The array can be divided into 2 contiguous subsegments:
Subsegments -> [2, 5, 1], [9, 7, 6]
Sorted subsegments -> [1, 2, 5], [6, 7, 9]
Final array -> [1, 2, 5, 6, 7, 9]

As the final arr is sorted, 2 is a possible answer.


The array can be divided into 3 contiguous subsegments:
Subsegments -> [2, 5, 1], [9, 7], [6]
Sorted Subsegments -> [1, 2, 5], [7, 9], [6]
Final array -> [1, 2, 5, 7, 9, 6]

As the combined arr is not sorted, 3 can't be possible.

Any higher number of subsegments will fail as well. The answer is 2.

findMaxSubsegmentsCount has the following parameter(s):
    int arr[n]:  the array of integers to partition

Returns
    int: the maximum number of contiguous subsegments in a valid set of partitions

Constraints
    1 ≤ n ≤ 105
    1 ≤ arr[i] ≤ 105

source: HackerRank
"""

# Maintain two arrays:
#   Prefix max: prefix_max[i] = max(arr[0], ..., arr[i])
#   Suffix min: suffix_min[i] = min(arr[i], ..., arr[n-1])

# These two arrays can be easily created using Dynamic programming.
# Now iterate over all the indexes and check whether the current index i can be a partition point or not.
# A given partition point can be considered in the set of good partitions only if prefix_max[i] <= suffix_min[i+1].
# Count the number of partition points. The number of partitions = number of partition points + 1.
import math


def findMaxSubsegmentsCount(arr):
    n = len(arr)

    suffix_min = [0] * (n + 1)
    suffix_min[n] = math.inf
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(suffix_min[i + 1], arr[i])

    prefix_max = -1
    res = 0
    for i, n in enumerate(arr):
        prefix_max = max(prefix_max, n)
        if prefix_max <= suffix_min[i + 1]:
            res += 1

    return res


findMaxSubsegmentsCount([2, 1, 3, 2, 4, 4, 5, 8, 7, 7])  # => 6
