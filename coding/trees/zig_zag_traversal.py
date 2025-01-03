"""

Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

"""
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque


def zigzag(root):
    if not root:
        return []

    result = []
    q = deque([root])
    reverse = False
    while q:
        level = deque()

        for _ in range(len(q)):
            node = q.popleft()
            if reverse:
                level.appendleft(node.val)
            else:
                level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)
        reverse = not reverse
    return result
