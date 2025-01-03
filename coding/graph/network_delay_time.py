import heapq
from collections import defaultdict

# Network Delay Time

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.


# Example
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    min_heap = [(0, k)]
    visited = {}

    while min_heap:
        time, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited[node] = time
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (time + weight, neighbor))

    if len(visited) == n:
        return max(visited.values())
    return -1


network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
