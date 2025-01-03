"""
INVERT BINARY TREE

Given the root of a binary tree, invert the tree, and return its root.

The inverse of an empty tree is the empty tree. The inverse of a tree with root "r",
subtrees 'right' and 'left', is a tree with root 'r' whose left subtree is inverse
of right, whose right subtree is inverse of left
"""

# https://leetcode.com/problems/invert-binary-tree/

# DFS recursive
def invert(root):
    if not root:
        return
    root.left, root.right = invert(root.right), invert(root.left)
    return root


# DFS iterative
def invert_iterative(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root


# Like BFS iterative
from collections import deque


def invert_bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
