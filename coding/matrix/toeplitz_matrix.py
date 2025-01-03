# 766. Toeplitz Matrix
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false. A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

def isToeplitzMatrix(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            print(matrix[i][j])
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True



def is_toeplitz(mat):

    rows, colums = len(mat), len(mat[0])
    def is_diagonal_same(row, col):
        val = matrix[row][vol]
        while row < rows and col < cols:
            if matrix[row][col] != val:
                return False
            row += 1
            col += 1
        return True

    for col in range(cols):
        if not is_diagonal_same(0, col):
            return False
    
    for row in range(1, rows):
        if not is_diagonal_same:
            return False


matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
isToeplitzMatrix(matrix)
