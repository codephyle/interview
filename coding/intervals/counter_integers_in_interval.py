# 2276. Count Integers in Intervals

# Given an empty set of intervals, implement a data structure that can:

# Add an interval to the set of intervals.
# Count the number of integers that are present in at least one interval.

# Implement the CountIntervals class:

#     CountIntervals() Initializes the object with an empty set of intervals.
#     void add(int left, int right) Adds the interval [left, right] to the set of intervals.
#     int count() Returns the number of integers that are present in at least one interval.
#     Note that an interval [left, right] denotes all the integers x where left <= x <= right.


# Example:

# Input
# ["CountIntervals", "add", "add", "count", "add", "count"]
# [[], [2, 3], [7, 10], [], [5, 8], []]

# Output
# [null, null, null, 6, null, 8]


# Explanation
# CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals.
# countIntervals.add(2, 3);  // add [2, 3] to the set of intervals.
# countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
# countIntervals.count();    // return 6
#                            // the integers 2 and 3 are present in the interval [2, 3].
#                            // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
# countIntervals.add(5, 8);  // add [5, 8] to the set of intervals.
# countIntervals.count();    // return 8

from sortedcontainers import SortedList

class CountIntervals:
    def __init__(self):
        self.intervals = SortedList()  # Store intervals sorted by start
        self.count = 0  # Track the count of unique integers covered

    def add(self, left, right):
        if left > right:
            return  # Ignore invalid intervals

        # Find overlapping intervals and merge them
        i = self.intervals.bisect_left((left,))
        while i < len(self.intervals) and self.intervals[i][1] < right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            self.count -= self.intervals[i][1] - self.intervals[i][0] + 1
            del self.intervals[i]

        # Check for partial overlap with the next interval
        if i < len(self.intervals) and self.intervals[i][0] <= right:
            right = max(right, self.intervals[i][1])
            self.count -= self.intervals[i][1] - self.intervals[i][0] + 1
            del self.intervals[i]

        self.intervals.add((left, right))
        self.count += right - left + 1

    def count(self):
        return self.count

# naive
class CountIntervals:
    def __init__(self):
        self.intervals = []

    def add(self, left, right):
        self.intervals.append((left, right))

    def count(self):
        nums = set()
        for interval in self.intervals:
            for num in range(interval[0], interval[1] + 1):
                nums.add(num)
        return len(nums)
