"""
MINIMUM DEPTH OF A BINARY TREE

Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""

from collections import deque


def min_depth(root):
    if not root:
        return 0
    q = deque([root])
    level = 0
    while q:
        level += 1
        for _ in range(len(q)):
            node = q.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    