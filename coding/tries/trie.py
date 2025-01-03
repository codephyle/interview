# Implement Trie (Prefix Tree)

# A trie or prefix tree is a tree data structure used to efficiently
# store and retrieve keys in a dataset of strings. There are various applications of this
# data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

#     Trie() - Initializes the trie object.
#     void insert(String word) - Inserts the string word into the trie.
#     boolean search(String word) - Returns true if the string word is in the trie (i.e., was inserted before),
#                                   and false otherwise.
#     boolean startsWith(String prefix) - Returns true if there is a previously inserted string word
#                                         that has the prefix prefix, and false otherwise.

# Input
#     ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#     [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
#     [null, null, true, false, true, null, true]

from collections import defaultdict


class Trie:

    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word):
        cur = self
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.isWord

    def prefix(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord == False


trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.startsWith("app") == True
trie.insert("app")
assert trie.search("app") == True


# Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.


# For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
def findWords(board, words):

    def dfs(node, i, j, path, res):
        if node.isWord:
            res.add(path)
            node.isWord = False  # avoid duplicate entries
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            dfs(node, x, y, path + tmp, res)
        board[i][j] = tmp

    trie = Trie()
    for word in words:
        trie.insert(word)
    res = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(trie, i, j, "", res)
    return list(res)


# Example usage:
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
print(findWords(board, words))  # Output: ['oath', 'eat']


# Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where the first subtree has nodes that are all smaller or equal to the target value, while the second subtree has all nodes that are greater than the target value. It is not necessarily the case that the tree contains a node with the value target.

# Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.


# Return an array of the two roots of the two subtrees in order.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def splitBST(root, target):
    if not root:
        return [None, None]

    if root.val <= target:
        left, right = splitBST(root.right, target)
        root.right = left
        return [root, right]
    else:
        left, right = splitBST(root.left, target)
        root.left = right
        return [left, root]


# Example usage:
# Construct the BST
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

target = 2
left_subtree, right_subtree = splitBST(root, target)
# The left_subtree should be the tree with nodes [1, 2] and the right_subtree should be the tree with nodes [3, 4, 5, 6, 7]
