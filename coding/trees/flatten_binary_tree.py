'''
114. FLATTEN BINARY TREE TO LINKED LIST

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list 
and the left child pointer is always null. The "linked list" should be in the same order as a pre-order traversal of the binary tree.

'''
def flattenTree(root):

    def flatten(node):
        if not node:
            return None
        
        # Flatten the left and right subtrees
        leftTail = flatten(node.left)
        rightTail = flatten(node.right)
        
        # If there was a left subtree, we shuffle the connections
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        
        # We need to return the "tail" of the flattened tree
        return rightTail or leftTail or node
    
    flatten(root)


def flatten(self, root: TreeNode) -> None:
    if not root:
        return
    
    stack = [root]
    while stack:
        current = stack.pop()
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        
        if stack:
            current.right = stack[-1]
        
        current.left = None
