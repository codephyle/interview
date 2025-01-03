"""
SAME TREE

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and 
the nodes have the same value.

"""
# https://leetcode.com/problems/same-tree/

def isSameTree(p, q):
    # reached a leaf
    if not p and not q:
        return True
    
    # one of the tree is empty while the other is not
    if not p or not q:
        return False
    
    # check the current node
    if p.val != q.val:
        return False
    
    # recurse
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    
