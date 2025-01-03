# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

from collections import Counter
import heapq


def topKFrequent(nums, k):
    freq = Counter(nums)
    sorted_nums = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    return sorted_nums[:k]


def top_k_frequent(nums, k):
    counter = Counter(nums)
    max_heap = [(-freq, num) for num, freq in counter.items()]
    heapq.heapify(max_heap)

    res = []
    for _ in range(k):
        res.append(heapq.heappop(max_heap)[1])

    return res


# without heap using bucket sort
def top_k_frequent_bucket(nums, k):
    
    freq = Counter(nums)
    bucket = [[] for _ in range(len(nums)+1)]

    for n,f in freq.items():
        bucket[f].append(n)
    
    res = []
    for i in range(len(bucket)-1, -1, -1):
        for num in bucket[i]:
            res.append(num)
            if k == len(res):
                return res


top_k_frequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3], 2)
top_k_frequent_bucket([1, 1, 1, 2, 2, 3, 3, 3, 3, 3], 2)
