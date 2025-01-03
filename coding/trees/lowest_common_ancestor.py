# Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

from tree import root


def path(root, goal):
    path, stack = [], [root]
    while True:
        node = stack.pop()
        if node:
            if node not in path[-1:]:
                path.append(node)
                if node == goal:
                    return path
                stack += node, node.right, node.left
            else:
                path.pop()


def lowestCommonAncestor(root, p, q):
    return next(a for a, b in list(zip(path(root, p), path(root, q)))[::-1] if a == b)


def lca(root, p, q):

    if root in (None, p, q):
        return root

    left, right = lca(root.left, p, q), lca(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right


print(lowestCommonAncestor(root, root.left.left, root.left.right.left).val)
print(lca(root, root.left.left, root.left.right.left).val)
