"""
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. 
You may assume that multiplication is always possible.


# Example usage
mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(multiply(mat1, mat2))  # Output: [[7,0,0],[-7,0,3]]

Example 1:
    Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
    Output: [[7,0,0],[-7,0,3]]

Example 2:
    Input: mat1 = [[0]], mat2 = [[0]]
    Output: [[0]]
"""

# https://leetcode.com/problems/sparse-matrix-multiplication/solution/


def multiply(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    k2, n = len(mat2), len(mat2[0])

    # Initialize the result matrix with zeros
    result = [[0] * n for _ in range(m)]

    # Iterate through each element of mat1
    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:
                # Multiply and add to the result matrix
                for l in range(n):
                    result[i][l] += mat1[i][j] * mat2[j][l]

    return result
