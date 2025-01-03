# Retrieve the k longest strings in a given streaming sequence of strings.

# As we read the stream, we should maintain a list of longest so-far seen strings.Once we process the first 'k' strings in the stream, we either have to remove the shortest string from the list, if the new string is longer the shortest string and add the new string to your list or discard the new string.

# To remove the shortest string, a min-heap of size 'k' will help us.

from itertools import islice
import heapq

def top(stream, k):
    heap = [(len(s), s) for s in islice(stream, k)]
    heapq.heapify(heap)
    for s in stream:
        smallest = heapq.nsmallest(1, heap)[0]
        if smallest[0] < len(s):
            heapq.heappushpop(heap, (len(s), s))
    return [len(p[1]) for p in heap]
