"""
SORT ARRAY BY INCREASING FREQUENCY

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order. Return the sorted array.

Examples:

    Input: nums = [1,1,2,2,2,3]
    Output: [3,1,1,2,2,2]
    Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

    Input: nums = [2,3,1,3,2]
    Output: [1,3,3,2,2]
    Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

    Input: nums = [-1,1,-6,4,5,-6,1,4,1]
    Output: [5,-1,4,4,-6,-6,1,1,1]
"""
from collections import Counter

def sortByFrequency(nums):
    freqs = Counter(nums).most_common()
    freqs.sort(key=lambda x: x[0], reverse=True)
    freqs.sort(key=lambda x: x[1])
    output = []
    for num, freq in freqs:
        output += [num] * freq
    return output

# aha!
def frequencySort(nums):
    freqs = Counter(nums)
    return sorted(nums, key=lambda x: (freqs[x], -x))

sortByFrequency([1,1,2,2,2,6,6,4,4,5,5,3])
frequencySort([1,1,2,2,2,6,6,4,4,5,5,3])