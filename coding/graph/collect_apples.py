# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

def minTimeToCollectApples(n, edges, hasApple):
    # Create an adjacency list to represent the tree
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Helper function to perform DFS traversal
    def dfs(node, parent):
        time = 0
        for child in graph[node]:
            if child != parent:
                time += dfs(child, node)
        # If the current node has an apple or it is not the starting node,
        # add 2 seconds to the total time
        if hasApple[node] or node != 0:
            time += 2
        return time
    
    # Start DFS traversal from vertex 0
    return dfs(0, -1)