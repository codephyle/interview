# 787. Cheapest Flights Within K Stops

# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

# Examples:

#     Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
#     Output: 700
#     Explanation: The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
#     Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

#     Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
#     Output: 200
#     Explanation: The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

#     Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
#     Output: 500
#     Explanation: The optimal path with no stops from city 0 to 2 is marked in red and has cost 500


import heapq
import collections

def findCheapestPrice(n, flights, src, dst, k):
    # Construct adjacency list representation of the graph
    graph = collections.defaultdict(set)

    for f, t, p in flights:
        graph[f].add((t, p))
    
    # Dijkstra's algorithm with modifications for maximum stops
    pq = [(0, src, -1)]  # Priority queue: (total cost, current city, stops)
    while pq:
        cost, city, stops = heapq.heappop(pq)
        if city == dst:
            return cost
        if stops < k:
            for neighbor, price in graph[city]:
                heapq.heappush(pq, (cost + price, neighbor, stops + 1))
    return -1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(findCheapestPrice(n, flights, src, dst, k)) 
