# 297. Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

from tree import Node
from collections import deque

def serialize(root):
    payload = []

    def dfs(node):
        if not node:
            return
        payload.append(str(node.val))
        for child in node.children:
            dfs(child)
        payload.append("#")  # indicates no more children

    dfs(root)
    return " ".join(payload)


def deserialize(payload):
    if not payload:
        return None

    tokens = deque(payload.split())
    root = Node(tokens.popleft(), [])

    def helper(node):

        if not tokens:
            return

        while tokens[0] != "#":  # add child nodes
            val = tokens.popleft()
            child = Node(int(val), [])
            node.children.append(child)
            helper(child)

        tokens.popleft()  # discard '#'

    helper(root)
    return root


root = Node(2)
five = Node(5)
five.children = [Node(4), Node(3)]
three = Node(3)
three.children = [Node(10)]
root.children = [Node(3), five, three, Node(7)]

# 2
#    3
#    5
#       4
#       3
#    3
#       10
#    7

print(serialize(deserialize(serialize(root))))
