# A container of integers that should support addition, removal, and search for the median integer

import heapq

class Container:
    def __init__(self):
        self.nums = []
        self.median = None
        self.lower_half = []
        self.upper_half = []

    def add(self, num):
        """
        Adds an integer to the container.
        """
        if self.median is None:
            self.median = num
        elif num <= self.median:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)
        
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))
        
        if len(self.lower_half) == len(self.upper_half):
            self.median = (-self.lower_half[0] + self.upper_half[0]) / 2
        else:
            self.median = -self.lower_half[0]

    def remove(self, num):
        """
        Removes an integer from the container.
        """
        if num == self.median:
            self.median = None
        elif num <= self.median:
            self.lower_half.remove(-num)
            heapq.heapify(self.lower_half)
        else:
            self.upper_half.remove(num)
            heapq.heapify(self.upper_half)

    def find_median(self):
        """
        Finds and returns the median integer in the container.
        """
        return self.median


import heapq

class Container:
    def __init__(self):
        self.lower_half = []  # Max-heap (negative values)
        self.upper_half = []  # Min-heap

    def add(self, num):
        """
        Adds an integer to the container.
        """
        if not self.lower_half or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)
        
        # Balance the heaps
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def remove(self, num):
        """
        Removes an integer from the container.
        """
        if num <= -self.lower_half[0]:
            # Remove from lower_half (max-heap)
            self._remove_from_heap(self.lower_half, -num)
        else:
            # Remove from upper_half (min-heap)
            self._remove_from_heap(self.upper_half, num)
        
        # Rebalance the heaps
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def _remove_from_heap(self, heap, num):
        """
        Helper function to remove an element from a heap.
        """
        idx = heap.index(num)  # Find the index of the number
        heap[idx] = heap[-1]  # Replace with the last element
        heap.pop()  # Remove the last element
        if idx < len(heap):
            heapq._siftup(heap, idx)  # Restore heap property
            heapq._siftdown(heap, 0, idx)

    def find_median(self):
        """
        Finds and returns the median integer in the container.
        """
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        elif len(self.upper_half) > len(self.lower_half):
            return self.upper_half[0]
        else:
            return (-self.lower_half[0] + self.upper_half[0]) / 2
