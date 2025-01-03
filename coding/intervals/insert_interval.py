# insert a new interval in a given sorted intervals
def insert(intervals, interval):

    if not intervals:
        return intervals

    merged = []
    i = 0
    n = len(intervals)

    # skip all the intervals which end before the start of the new interval
    while i < n and intervals[i][1] < interval[0]:
        merged.append(intervals[i])
        i += 1

    # merge all intervals that overlap with the new interval
    while i < n and intervals[i][0] <= interval[1]:
        interval[0] = min(intervals[i][0], interval[0])
        interval[1] = max(intervals[i][1], interval[1])
        i += 1

    merged.append(interval)

    # add all the remainind intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


insert([[1, 3], [5, 7], [8, 12]], [4, 6])
insert([[1, 3], [5, 7], [8, 12]], [4, 10])
insert([[2, 3], [5, 7]], [1, 4])
