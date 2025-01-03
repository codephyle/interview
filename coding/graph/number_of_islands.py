"""
NUMBER OF ISLANDS

Given an 'm x n' 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically.

You may assume all four edges of the grid are all surrounded by water.

Using union-find  https://leetcode.com/problems/number-of-islands-ii/discuss/75468/Compact-Python

"""


# DFS solution
def number_of_islands(grid):

    if not grid:
        return None

    def dfs(i, j):
        # check boundary and land
        if i < 0 or j < 0 or i >= rows or j >= columns or grid[i][j] != "1":
            return

        grid[i][j] = "#"  # mark visited
        # visited[i][j] = True
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i - 1, j)
        dfs(i + 1, j)

    rows, columns = len(grid), len(grid[0])
    count = 0

    # visited = [[False for _ in range(c)] for _ in range(r)]

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == "1":
                dfs(i, j)
                count += 1
    return count


# BFS Solution
from collections import deque


def num_of_islands(grid):
    if not grid:
        return 0

    def bfs(r, c):
        if grid[r][c] == "0":
            return 0
        queue = deque([(r, c)])
        while queue:
            r, c = queue.popleft()

            if r - 1 >= 0 and grid[r - 1][c] == "1":
                queue.append((r - 1, c))
                grid[r - 1][c] = "0"

            if r + 1 < len(grid) and grid[r + 1][c] == "1":
                queue.append((r + 1, c))
                grid[r + 1][c] = "0"

            if c - 1 >= 0 and grid[r][c - 1] == "1":
                queue.append((r, c - 1))
                grid[r][c - 1] = "0"

            if c + 1 < len(grid[0]) and grid[r][c + 1] == "1":
                queue.append((r, c + 1))
                grid[r][c + 1] = "0"
        return 1

    ans = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                ans += bfs(r, c)
    return ans


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
number_of_islands(grid)

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

num_of_islands(grid)
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
number_of_islands(grid)

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
num_of_islands(grid)

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]


def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])


def ones(grid):

    rows = len(grid)
    cols = len(grid[0])

    count = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
            return

        grid[i][j] = "#"
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

        print_grid(grid)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                dfs(i, j)
                count += 1
    print(count)


ones(grid)
