# 938. Range Sum of BST

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

def range_sum(root, low, high):

    total = 0

    def dfs(root):
        nonlocal total

        if not root:
            return

        if low <= root.val <= high:
            total += root.val
        
        if root.val > low:
            dfs(root.left)
        
        if root.val < high:
            dfs(root.right)

    dfs(root)
    return total


def range_sum_iter(root, low, high):

    stack = [root]
    total = 0

    while stack:
        node = stack.pop()
        if low <= node.val <= high:
            total += node.val

        if node.val > low and node.left: # we have no None check
            stack.append(node.left)
        
        if node.val < high and node.right:
            stack.append(node.right)

    return total


# root = [10,5,15,3,7,null,18]
# low, high = 7, 15
