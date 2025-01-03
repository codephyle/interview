"""
CONNECT LEVEL ORDER SIBLINGS 

Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to a null node.
"""

from collections import deque


def connect_siblings(root):
    if not root:
        return None
    q = deque([root])
    while q:
        prev = None
        for _ in range(len(q)):
            curr = q.popleft()
            if prev:
                prev.next = curr
            prev = curr
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)


def connect_all_siblings(root):
    if not root:
        return None
    q = deque([root])
    curr, prev = None, None
    while q:
        curr = q.popleft()
        if prev:
            prev.next = curr
        prev = curr
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

