class Node:
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


# recursive
def clone_dfs(node):

    if not node:
        return node

    # keep track of cloned nodes
    clones = {}

    def dfs(node):

        # after all we need only one clone. this avoid we getting into infinite loop
        if node in clones:
            return clones[node]

        clone = Node(node.val)
        clones[node] = clone  # remember we cloned

        clone.neighbors = []
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


# iterative
from collections import deque


# Use a map to store visited/cloned nodes
def clone_bfs(node):

    # empty graph
    if not node:
        return None

    queue = deque([node])
    clones = {node: Node(node.val)}

    while queue:
        curr = queue.popleft()
        clone = clones[curr]
        for neighbor in curr.neighbors:
            if neighbor not in clones:
                clones[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            clone.neighbors.append(clones[neighbor])

    return clones[node]
