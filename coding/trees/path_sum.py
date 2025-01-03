# BINARY TREE PATH SUM

# Given a binary tree and a number "S", find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals "S".

def has_path_with_sum(root, target):
    
    if not root:
        return False

    target -= root.val
    if not root.left and not root.right: # leaf node
        return target == 0

    return has_path_with_sum(root.left, target) or has_path_with_sum(root.right, target)


def has_path(root, target):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == target:
            return True
        if curr.right:
            stack.append((curr.right, curr.right.val + val))
        if curr.left:
            stack.append((curr.left, curr.left.val + val))

    return False

"""

Given a binary tree and a number "S", 
find all paths from root-to-leaf such that the sum of all the node values of each path equals "S"

"""

def all_paths(root, target):
    if not root:
        return []

    result = []
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == target:
            result.append() 


def all_paths(root, target):

    def dfs(root, target, path, all):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and target == root.val:
                all.append(list(path)) 
        if root.left:
            dfs(root.left, target - root.val, path, all)
        if root.right:
            dfs(root.right, target - root.val, path, all)

        del path[-1]

    all = []
    dfs(root, target, [], all)
    print(all)

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

all_paths(root, 18)
