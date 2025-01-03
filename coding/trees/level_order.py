"""
BINARY TREE LEVEL ORDER TRAVERSAL

Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

"""
# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque


def level_order(root):
    result = []
    if not root:
        return result

    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        result.append(level)

    return result


def level_order_dfs(root):
    result = []
    if not root:
        return result

    def dfs(root, level):
        if len(result) == level:
            result[level] = []
        result[level].append(root.val)
        if root.left:
            dfs(root.left, level + 1)
        if root.right:
            dfs(root.right, level + 1)

    dfs(root, 0)
    return result


# Variants
