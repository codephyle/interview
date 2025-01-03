# 1691. Maximum Height by Stacking Cuboids 

# Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

# You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

# Return the maximum height of the stacked cuboids.

# Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# Output: 190
# Explanation:
#     Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
#     Cuboid 0 is placed next with the 45x20 side facing down with height 50.
#     Cuboid 2 is placed next with the 23x12 side facing down with height 45.
# The total height is 95 + 50 + 45 = 190.

# Example 2:
# Input: cuboids = [[38,25,45],[76,35,3]]
# Output: 76
# Explanation:
#     You can't place any of the cuboids on the other.
#     We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.

def max_height(boxes):
    # Generate rotations of boxes
    rotations = []
    for box in boxes:
        rotations.append((box[0], box[1], box[2]))  # original orientation
        rotations.append((box[1], box[0], box[2]))  # rotate width and length
        rotations.append((box[2], box[0], box[1]))  # rotate height and length

    # Sort rotations by base area in descending order
    rotations.sort(key=lambda x: x[0] * x[1], reverse=True)

    # Initialize dp array to store maximum heights
    n = len(rotations)
    dp = [0] * n

    # Compute maximum height for each rotation
    for i in range(n):
        length, width, height = rotations[i]
        dp[i] = height  # base case

        for j in range(i):
            if rotations[j][0] > length and rotations[j][1] > width:
                dp[i] = max(dp[i], dp[j] + height)

    return max(dp)

# Example usage:
boxes = [(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)]
print(max_height(boxes))  # Output: 60


def maxHeight(self, A):
    A = [[0, 0, 0]] + sorted(map(sorted, A))
    dp = [0] * len(A)
    for j in xrange(1, len(A)):
        for i in xrange(j):
            if all(A[i][k] <= A[j][k] for k in xrange(3)):
                dp[j] = max(dp[j], dp[i] + A[j][2])
    return max(dp)