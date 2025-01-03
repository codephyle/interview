from collections import deque

# BFS successsor will be in the front of the queue, as it is going to be removed/processed next

def bfs_successor(root, val):
    if not root:
        return None

    q = deque([root])
    while q:
        n = q.popleft()
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
        if n.val == val:
            break
    return q[0] if q else None


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
    root.left.right = Node(-3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(9)
    #             1
    #     2                3
    # 4     3         5        6
    #             7     8   9
    return root


n = bfs_successor(bt(), -3)
print(n.val)
