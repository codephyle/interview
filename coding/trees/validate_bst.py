# 98. VALIDATE BINARY SEARCH TREE
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.

# https://leetcode.com/problems/validate-binary-search-tree/
def valid_bst(root):

    def valid(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root)


def valid_bst_iterative(root):
    if not root:
        return True

    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        node, low, high = stack.pop()
        if not (low < node.val < high):
            return False
        stack.append(node.left, low, node.val)
        stack.append(node.right, node.val, high)

    return True
