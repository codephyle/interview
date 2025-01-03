# 286. Walls and Gates

# You are given an m x n grid rooms initialized with these three possible values.

#   * -1 A wall or an obstacle.
#   * 0 A gate.
#   * INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example 1:

#     Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
#     Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

#     Input: rooms = [[-1]]
#     Output: [[-1]]

from collections import deque

EMPTY = float('inf')  # Python equivalent of Integer.MAX_VALUE
GATE = 0
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def walls_and_gates(rooms):
    if not rooms:
        return

    rows = len(rooms)
    cols = len(rooms[0])
    queue = deque()

    # Enqueue all gates
    for row in range(rows):
        for col in range(cols):
            if rooms[row][col] == GATE:
                queue.append((row, col))

    # BFS to calculate distances
    while queue:
        row, col = queue.popleft()
        for dr, dc in DIRECTIONS:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and rooms[r][c] == EMPTY:
                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))