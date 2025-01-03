# RIGHT VIEW OF A BINARY TREE

# Given a binary tree, return an array containing nodes in its right view. 
# The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

from collections import deque

def right_view(root):
    if not root:
        return []

    result = []
    q = deque([root])
    while q:
        result.append(q[-1])
        for _ in range(len(q)):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return result
