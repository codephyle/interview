"""
Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Examples:
    matrix = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].

    matrix = [
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

    matrix = [[1]]
    Output: 1

"""
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/solution/
from functools import lru_cache

def longestIncrPath(matrix):

    if not matrix or not matrix[0]:
        return 0

    @lru_cache
    def dfs(i, j):
        val = matrix[i][j]
        
        # up
        if i > 0 and matrix[i-1][j] > val:
            up = dfs(i-1, j)
        else:
            up = 0

        # down
        if i < rows-1  and matrix[i+1][j] > val:
            down = dfs(i+1, j)
        else:
            down = 0
        
        # left
        if j > 0 and matrix[i][j-1] > val:
            left = dfs(i, j-1)
        else:
            left = 0

        # right
        if j < columns-1 and matrix[i][j+1] > val:
            right = dfs(i, j+1)
        else:
            right = 0

        return 1 + max(up, down, left, right)
        
    rows, columns = len(matrix), len(matrix[0])
    print(rows, columns)
    longest = 0
    for i in range(rows):
        for j in range(columns):
            print(i, j)
            longest = max(longest, dfs(i, j))

    return longest

longestIncrPath([
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ])

