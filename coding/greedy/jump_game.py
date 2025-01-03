"""
JUMP GAME

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
def can_jump(nums):
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
        # Early Termination
        if reach >= len(nums):
            return True
    return True


can_jump([2, 4, 1, 1, 0, 2, 3])


"""
Jump Game II - MINIMUM JUMPS

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

"""


def min_jumps(nums):
    jumps = 0
    l, r = 0, 0
    while r < len(nums) - 1:
        jumps += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, nxt
    return jumps


assert min_jumps([2, 3, 1, 1, 4]) == 2
assert min_jumps([2, 3, 0, 1, 4]) == 2

"""
Jump Game III ***

Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
"""

# recursive
def can_reach(A, i):
    if 0 <= i < len(A) and A[i] >= 0:
        A[i] = -A[i]
        return A[i] == 0 or can_reach(A, i + A[i]) or can_reach(A, i - A[i])
    return False


# iterative (bfs)

# def canReach(self, arr: List[int], start: int) -> bool:
#     n = len(arr)
#     q = [start]

#     while q:
#         node = q.pop(0)
#         # check if reach zero
#         if arr[node] == 0:
#             return True
#         if arr[node] < 0:
#             continue

#         # check available next steps
#         for i in [node + arr[node], node - arr[node]]:
#             if 0 <= i < n:
#                 q.append(i)

#         # mark as visited
#         arr[node] = -arr[node]

#     return False


"""
JUMP GAME IV

You are given a 0-indexed binary string s and two integers minJump and maxJump. 
In the beginning, you are standing at index 0, which is equal to '0'. You can move from 
index i to index j if the following conditions are fulfilled:

    - i + minJump <= j <= min(i + maxJump, s.length - 1), and
    - s[j] == '0'.

Return true if you can reach index s.length - 1 in s, or false otherwise.

"""

# def canReach(self, s, minJ, maxJ):
#     dp = [c == '0' for c in s]
#     pre = 0
#     for i in xrange(1, len(s)):
#         if i >= minJ: pre += dp[i - minJ]
#         if i > maxJ: pre -= dp[i - maxJ - 1]
#         dp[i] &= pre > 0
#     return dp[-1]


# def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
#     queue = collections.deque([0])
#     mx = 0
#     while queue:
#         i = queue.popleft()
#         for j in range(max(i + minJump, mx + 1), min(i + maxJump + 1, len(s))):
#             if s[j] == '0':
#                 if j == len(s) - 1: return True
#                 queue.append(j)
#         # mx = max(mx, i + maxJump)
# 		mx = i + maxJump # thanks @migeater pointd out that it's kind of topological sort, which means mx will always be larger while performing BFS
#     return False
