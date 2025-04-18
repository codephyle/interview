# 1293. Shortest Path in a Grid with Obstacles Elimination

# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: The shortest path without eliminating any obstacle is 10. The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.

def shortestPathWithObstacles(grid, k):
    m, n = len(grid), len(grid[0])

    # grid of size 1
    if m == n == 1:
        return 0 if grid[0][0] == 0 else -1

    # number of obstacles greater than shortest path
    if k >= m + n - 2:
        return m + n - 2

    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    q = deque([(0,0,0,0)]) # (x, y, steps, eliminated)
    seen = { (0,0): 0 }

    # understand and uncomment
        # while queue:
        # x, y, steps, eliminated = queue.popleft()
        
        # # Explore all 4 possible directions
        # for dx, dy in directions:
        #     nx, ny = x + dx, y + dy
            
        #     if 0 <= nx < m and 0 <= ny < n:
        #         new_eliminated = eliminated + grid[nx][ny]
                
        #         if new_eliminated <= k:
        #             if (nx, ny) == (m - 1, n - 1):
        #                 return steps + 1
                    
        #             if (nx, ny) not in visited or visited[(nx, ny)] > new_eliminated:
        #                 visited[(nx, ny)] = new_eliminated
        #                 queue.append((nx, ny, steps + 1, new_eliminated))