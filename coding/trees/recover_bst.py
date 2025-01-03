# RECOVER BINARY SEARCH TREE

# You are given the root of a binary search tree (BST), where the values of exactly two nodes
# of the tree were swapped by mistake. Recover the tree without changing its structure.

# https://leetcode.com/problems/recover-binary-search-tree/solution/


def recover_bst(root):
    # get inorder list
    # find the swapped elements
    # traverse again and change the values
    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)

    def swapped(nums):
        x = y = None
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                y = nums[i + 1]
                if x is None:
                    x = nums[i]
                else:
                    break
        return x, y

    def recover(root, count):
        if not root:
            return

        if root.val in (x, y):
            root.val = y if root.val == x else x

        recover(root.left, count - 1)
        recover(root.right, count - 1)

    x, y = swapped(inorder(root))
    recover(root, x, y, 2)
