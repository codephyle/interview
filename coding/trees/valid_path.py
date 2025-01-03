'''
FIND IF PATH EXISTS IN GRAPH

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge 
between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, 
or false otherwise.

Examples
    Input: n = 3, edges = [[0,1], [1,2], [2,0]], source = 0, destination = 2
    Output: true
    Explanation: There are two paths from vertex 0 to vertex 2:
    - 0 → 1 → 2
    - 0 → 2

    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
    Explanation: There is no path from vertex 0 to vertex 5.
'''
def validPath(n, edges, start, end):

    graph = [set() for _ in range(n)]
    for s, e in edges:
        graph[s].add(e)
        graph[e].add(s)

    stack = [start]
    visited = set()
    while stack:
        curr = stack.pop()
        if curr == end:
            return True
        if curr in visited:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            stack.append(neighbor)
        
    return False


from collections import defaultdict
def validPath(n, edges, start, end):
    graph = defaultdict(list)
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    
    def dfs(root):
        if root == end:
            return True
        if root in visited:
            return False
        visited.add(root)
        for neighbor in graph[root]:
            if dfs(neighbor):
                return True
        return False

    visited = set()
    return dfs(start)


# BFS
from collections import deque
def validPath(n, edges, start, end):
    graph = defaultdict(list)
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)

    visited = set()    
    q = deque([start])
    while q:
        curr = q.popleft()
        if curr == end:
            return True
        if curr in visited:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                q.append(neighbor)
        
    return False
         
    

validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)
validPath(3, [[0,1], [1,2], [2,0]], 0, 2)
        