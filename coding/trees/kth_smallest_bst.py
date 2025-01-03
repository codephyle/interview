"""
Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# can be improved
def kth_smallest_bst(root, k):
    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)

    return inorder(root)[k - 1]


# iterative
def kth_smallest_bst_iterative(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if not k:
            return root.val

        root = root.right
