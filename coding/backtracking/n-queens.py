"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

    Input: n = 1
    Output: [["Q"]]
"""


def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_nqueens_util(board, col, n):
    # If all queens are placed, then return True
    if col >= n:
        print_solution(board)
        return True
    
    res = False
    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 'Q'
            
            # Make result true if any placement is possible
            res = solve_nqueens_util(board, col + 1, n) or res
            
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col] (backtrack)
            board[i][col] = '.'
    
    return res

def solve_nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0, n):
        print("Solution does not exist")
        return False
    return True

def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()
    
# Example usage
solve_nqueens(4)
