# 684. Redundant Connection

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# Example 1:
#     Input: edges = [[1,2],[1,3],[2,3]]
#     Output: [2,3]

# Example 2:
#     Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
#     Output: [1,4]

from collections import defaultdict, deque

def redundant_connection(edges):
    
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(c)
    
    for u,v in edges:
        queue = deque[(u, -1)]
        visited = set()
        while queue:
            node, parent = queue.popleft()
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if niegh in visited:
                    return [u,v]
                visited.add(neigh)
                queue.append((neigh, node))
    return []

    
# UNION-FIND
def findRedundantConnection(edges):
    parent = list(range(len(edges) + 1))  # Create a parent array for Union-Find

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression optimization
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    for u, v in edges:
        if find(u) == find(v):  # Cycle detected
            return [u, v] 
        union(u, v)  # Merge sets if no cycle

    return [] 