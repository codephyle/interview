from tree import Node

def bst():
    root = Node(50)
    root.left = Node(25)
    root.right = Node(100)
    root.left.left = Node(15)
    root.left.right = Node(40)
    root.left.right.left = Node(30)
    root.right.left = Node(75)
    root.right.right = Node(125)
    root.right.left.left = Node(70)
    root.right.left.right = Node(90)
    return root


def bt():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(9)
    return root


# Given a binary tree and a number ‘S’,
# find if the tree has a path from root-to-leaf such that
# the sum of all the node values of that path equals ‘S’.
def path_sum(root, S):

    if not root:
        return False

    if root.left is None and root.right is None and root.val == S:
        return True

    return path_sum(root.left, S - root.val) or path_sum(root.right, S - root.val)


# Given a binary tree and a number ‘S’,
# find all paths from root-to-leaf such that
# the sum of all the node values of each path equals ‘S’.


def all_paths_sum(root, S):

    paths = []
    paths_to_leaf(root, S, [], paths)
    return paths


def paths_to_leaf(root, S, path, paths):

    if not root:
        return

    path.append(root.val)

    if path.left is None and path.right is None:
        if sum(path) == S:
            paths.append(list(path))
    else:
        paths_to_leaf(root.left, path, paths)
        paths_to_leaf(root.right, path, paths)

    del path[-1]


# SUM OF PATH NUMBERS

# Given a binary tree where each node can only have a digit (0-9) value,
# each root-to-leaf path will represent a number.
# Find the total sum of all the numbers represented by all paths.


def sum_of_path_numbers(root):
    def f(root, pathsum):

        if not root:
            return 0

        pathsum = pathsum * 10 + root.val

        if root.left is None and root.right is None:
            return pathsum

        return f(root.left, pathsum) + f(root.right, pathsum)

    return f(root, 0)


# PATH WITH GIVEN SEQUENCE
#
# Given a binary tree and a number sequence,
# find if the sequence is present as a root-to-leaf path in the given tree.


def path(root, seq):
    if not root:
        return False

    if root.val != seq[0]:
        return False

    if root.left is None and root.right is None and len(seq) == 1:
        return True

    return path(root.left, seq[1:]) or path(root.right, seq[1:])


# COUNT PATHS FOR A SUM
#
# Given a binary tree and a number ‘S’,
# find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
# Please note that the paths can start or end at any node,
# but all paths must follow direction from parent to child (top to bottom).

# FIX THIS
def paths_with_sum(root, s):
    def f(root, s, path, paths):

        if not root:
            return

        path.append(root.val)

        if sum(path) == s:
            paths.append(list(path))

        f(root.left, s, path, paths)
        f(root.right, s, path, paths)

        del path[-1]

    paths = []
    f(root, s, [], paths)


# BINARY TREE MAXIMUM PATH SUM
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
# in the sequence has an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

max_path_sum = 0


def calc_pathsum(root):

    global max_path_sum

    if not root:
        return 0

    lsum = calc_pathsum(root.left)
    rsum = calc_pathsum(root.right)

    lsum = max(lsum, 0)
    rsum = max(rsum, 0)

    curr_sum = lsum + rsum + root.val
    max_path_sum = max(max_path_sum, curr_sum)

    return curr_sum
