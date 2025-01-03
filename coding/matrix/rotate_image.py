# ROTATE IMAGE

# You are given an n x n 2D matrix representing an image,
# rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have
# to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.

# https://leetcode.com/problems/rotate-image/

# Input: [ [1,2,3],
#          [4,5,6],
#          [7,8,9] ]
# Output: [[7,4,1],
#          [8,5,2],
#          [9,6,3] ]

# Input: [[5,1,9,11],
        # [2,4,8,10],
        # [13,3,6,7],
        # [15,14,12,16]]
# Output: [
    #    [15,13,2,5],
    #    [14,3,4,1],
    #    [12,6,8,9],
    #    [16,7,10,11]]

# aha!
def rotate(A):
    A[:] = zip(*A[::-1])


def rotate(A):
    A.reverse()
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
