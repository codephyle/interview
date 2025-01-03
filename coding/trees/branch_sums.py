""" 
BRANCH SUMS - BINARY TREE

Write a function that takes in a Binary Tree and returns a list of its branch sums ordered 
from leftmost branch sum to rightmost branch sum. A branch sum is the sum of all values in a Binary Tree branch. 

A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node. 
"""


# binary tree path sums
def paths(root):

    if not root:
        return []

    def dfs(root, pathsum):
        if not root:
            return

        if not root.left and not root.right:
            sums.append(pathsum + root.val)

        if root.left:
            dfs(root.left, pathsum + root.val)

        if root.right:
            dfs(root.right, pathsum + root.val)

    sums = []
    dfs(root, 0)
    return sums


def pathsums(root):

    if not root:
        return []

    stack, output = [root], []
    currSum = 0
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            output.append(currSum)

        if node.right:
            currSum += node.val
            stack.append(node.right)

        if node.left:
            currSum += node.val
            stack.append(node.left)

        print(currSum)

        # print("after. " + str(currSum))

    return output


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bt():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(3)
    # root.right.left = Node(5)
    # root.right.right = Node(6)
    # root.right.left.left = Node(7)
    # root.right.left.right = Node(8)
    # root.right.right.left = Node(9)
    #             1
    #     2                3
    # 4     3         5        6
    #             7     8   9
    return root


paths(bt())
pathsums(bt())
