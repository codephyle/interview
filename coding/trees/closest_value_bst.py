"""
FIND CLOSEST VALUE IN BST

Write a function that takes in a Binary Search Tree (BST) and a target integer value 
and returns the closest value to that target value contained in the BST.
"""
def closest(root, target):
    if not root:
        return None
    closest = root.val
    while root:
        if abs(target-root.val) < abs(target-closest):
            closest = root.val
        root = root.left if target < root.val else root.right
    return closest
