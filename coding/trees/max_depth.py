"""
MAXIMUM DEPTH OF BINARY TREE

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

"""
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


# TODO solve iteratively 