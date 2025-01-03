"""
FIND THE MEDIAN OF A NUMBER STREAM

Design a class to calculate the median of a number stream. The class should have the following two methods:

    add(int num): stores the number in the class
    findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Input
    ["MedianFinder", "add", "add", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]

Output
    [null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

"""
# Idea is to maintain two heaps
#  1. max heap to store smaller elements
#  2. min heap to store larger elements
from heapq import *

class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def add(self, n):
        small, large = self.heaps
        if len(small) == len(large):
            x = heappushpop(large, n)
            heappush(small, -x)
        else:
            x = heappushpop(small, -n)
            heappush(large, -x)

    def findMedian(self):
        small, large = self.heaps
        if len(small) == len(large):
            return (-small[0] + large[0]) / 2.0
        return -small[0] / 1.0


medianFinder = MedianFinder()
medianFinder.add(1)
# arr = [1]
medianFinder.add(2)
# arr = [1, 2]
medianFinder.findMedian()
# return 1.5 (i.e., (1 + 2) / 2)
medianFinder.add(3)
# arr[1, 2, 3]
medianFinder.findMedian()
# return 2.0

[5, 10,100,200,6,13,14,50,51,52,1000]