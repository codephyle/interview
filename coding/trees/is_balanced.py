"""
BALANCED BINARY TREE TEST

Write a function to see if a binary tree is "superbalanced".

A tree is "superbalanced" if the difference between the depths of any two leaf nodes
is no greater than one.
"""


def is_balanced(root):
    if not root:
        return True

    depths = set()
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()
        # leaf
        if not node.left and not node.right:
            if depth not in depths:
                depths.append(depth)
            if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1])) > 1:
                return False
        else:
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

    return True


# recursive
def is_balanced_dfs(root):

    # Height of a node
    def height(root):
        if not root:
            return 0
        return 1 + max(height(root.left), height(root.right))

    if not root:
        return True

    return (
        abs(height(root.left) - height(root.weight) < 2)
        and is_balanced_dfs(root.left)
        and is_balanced_dfs(root.right)
    )
