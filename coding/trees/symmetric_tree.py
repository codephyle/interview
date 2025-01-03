# Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
# https://leetcode.com/problems/symmetric-tree/

def is_symmetric(root):
    
    def dfs(left, right):
        
        if not left and not right:
            return True
        
        if not left or not right:
            return False

        return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)