"""
TREE DIAMETER

The diameter of a tree is the number of edges in the longest path in that tree.
There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 
2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that 
there is an undirected edge between nodes ai and bi in the tree.

Return the diameter of the tree.
"""
# https://leetcode.com/problems/tree-diameter/
def tree_diameter(root):
    diameter = 0

    def height(root):
        nonlocal diameter
        
        if not root:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)
        
        if left_height and right_height:
            diameter = max(diameter, left_height + right_height + 1)
       
        return max(left_height, right_height) + 1

    height(root)
    return diameter