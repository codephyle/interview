# WORD SEARCH

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Examples:
#     board = [ ["A","B","C","E"],
#               ["S","F","C","S"],
#               ["A","D","E","E"]], 
#         word = "ABCCED"  => True
#         word = "SEE"     => True
#         word = "ABCB"    => False

def exist(board, word):

    rows, columns = len(board), len(board[0]) 

    def backtrack(i, j, index):

        if index == len(word):
            return True

        if ( i < 0 or i >= rows or
             j < 0 or j >= columns or 
             board[i][j] != word[index]):
             return False
        
        tmp = board[i][j]
        board[i][j] = "#"

        ret = backtrack(i, j+1, index+1) or backtrack(i, j-1, index+1) or backtrack(i+1, j, index+1) or backtrack(i-1, j, index+1)

        board[i][j] = tmp
        return ret


    for i in range(rows):
        for j in range(columns):
            if backtrack(i,j,0):
                return True

    
    return False

        
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

print(exist(board, word1))  # Output: True
print(board)

print(exist(board, word2))  # Output: True
print(exist(board, word3))  # Output: False