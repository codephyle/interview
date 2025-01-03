"""
LOWEST STARTING STAIR

A monkey is jumping on a long staircase, on which each stair is numbered; the bottommost stair being 1, the next stair being 2, and so on. 
In one jump, it can go some steps up or down. Given an array jumps of integers representing each jump of the monkey as:

If jumps[i] > 0, the monkey jumps jumps[i] steps up from its current step.
If jumps[i] < 0, the monkey jumps |jumps[i] | steps down from its current step.

Find the number of the lowest stair, startingStair on which the monkey should start so that it can remain on the staircase; that is, the stair number remains >= 1.

Example

jumps = [1, -4, -2, 3]. 

If startingStair= 6, the following results are obtained:

Stair    jumps[i]
-----     -----
6           1
7          -4
3          -2
1           3
4
 

For startingStair = 6, the stair number remains >=1 throughout the jumps. 
This is the least possible value of startingStair for the condition to be true. Therefore, the answer is 6.

Function Description
    Complete the function findLowestStartingStair in the editor below.
    findLowestStartingStair has the following parameter:
        int jumps[n]:  an array of integers

Returns
    int: the minimum integer value for startingStair.

Constraints
    1 ≤ n ≤ 105
    −100 ≤ jumps[i] ≤ 100

source: HackerRank
"""
