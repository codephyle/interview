# Point
class Point:
    def __init__(self, props):
        self.props = props

    def __getitem__(self, depth):
        return self.props(depth % len(self.props))

    def __len__(self):
        return len(self.props)

    def __repr__(self):
        return str(self.props)


# Node
class Node:
    def __init__(self, point):
        self.point = point
        self.left = self.right = None


class KdTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        if not self.root:
            self.root = node
        else:
            self._insert(node, 0)

    def _insert(self, node, k):
        if node.point[k] < self.root.point[k]:
            if self.root.left == None:
                self.root.left = node
            else:
                self.insert(self.root.left, k + 1)

        else:

            if self.root.right == None:
                self.root.right = node
            else:
                self.insert(self.root.right, k + 1)
