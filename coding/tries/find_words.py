# Given an m x n board of characters and a list of strings words, return all words on the board.


# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


def find_words(board, words):
    def dfs(node, i, j, path, res):
        if node.is_end_of_word:
            res.add(path)
            node.is_end_of_word = False  # Avoid duplicate entries

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        char = board[i][j]
        if char not in node.children:
            return

        board[i][j] = "#"  # Mark the cell as visited
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(node.children[char], i + x, j + y, path + char, res)
        board[i][j] = char  # Unmark the cell

    trie = Trie()
    for word in words:
        trie.insert(word)

    res = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(trie.root, i, j, "", res)

    return list(res)
