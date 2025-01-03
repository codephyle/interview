from itertools import islice
import heapq


def top(stream, k):
    heap = [(len(s), s) for s in islice(stream, k)]
    heapq.heapify(heap)
    for s in stream:
        smallest = heapq.nsmallest(1, heap)[0]
        # print(heap[0][0], len(s), smallest)
        if smallest[0] < len(s):
            heapq.heappushpop(heap, (len(s), s))
    return [len(p[1]) for p in heap]
