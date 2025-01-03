# in-order [left, root, right]
def inorder(root):
    stack, output = [], []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            output.append(temp.val)
            root = temp.right
    return output


# preorder [root, left, right]
def preorder(root):
    if not root:
        return []
    stack, output = [root], []
    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return output


# post-order [left, right, root]
def postorder(root):
    if not root:
        return []

    stack, output = [root], []
    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

    return output[::-1]
