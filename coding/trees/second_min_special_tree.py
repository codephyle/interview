# Second Minimum Node In a Binary Tree
#
# Given a non-empty special binary tree consisting of nodes with the non-negative value,
# where each node in this tree has exactly two or zero sub-node.
# If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
# More formally, the property root.val = min(root.left.val, root.right.val) always holds.
#
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.

# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

def second_min_special_tree(root):
    
    first = root.val
    second = float(inf)

    def dfs(node):

        nonlocal first
        nonlocal second

        if not node:
            return

        if first < node.val < second:
            second = node.val
        
        if first == node.val and node.left:
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    
    return second if second != float('inf') else -1
