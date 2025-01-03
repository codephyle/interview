# 310. Minimum Height Trees

# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# https://leetcode.com/problems/minimum-height-trees/

from collections import defaultdict, deque


def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]

    # Build adjacency list
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Initialize a queue with leaf nodes
    leaves = deque()
    for node in adj_list:
        if len(adj_list[node]) == 1:
            leaves.append(node)

    remaining_nodes = n
    while remaining_nodes > 2:
        num_leaves = len(leaves)
        remaining_nodes -= num_leaves

        # Remove current leaf nodes and update adjacency list
        for _ in range(num_leaves):
            leaf = leaves.popleft()
            neighbor = adj_list[leaf].pop()
            adj_list[neighbor].remove(leaf)

            # If the neighbor becomes a leaf node, add it to the queue
            if len(adj_list[neighbor]) == 1:
                leaves.append(neighbor)

    # The remaining nodes in the queue are the roots of minimum height trees
    return list(leaves)
