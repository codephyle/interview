from collections import deque

# You are given an m x n grid grid where:

# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
# You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

# If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

# Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

# Input: grid = ["@.a..","###.#","b.A.B"]
# Output: 8
# Explanation: Note that the goal is to obtain all the keys not to open all the locks.


def shortest_path_to_get_all_keys(grid):
    # Define the four cardinal directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Find the starting position and count the number of keys
    start_row, start_col = 0, 0
    num_keys = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                start_row, start_col = i, j
            elif grid[i][j].islower():
                num_keys += 1

    # Initialize the queue for BFS
    queue = deque([(start_row, start_col, "")])
    visited = set([(start_row, start_col, "")])

    # Perform BFS
    while queue:
        row, col, keys = queue.popleft()

        # Check if all keys have been collected
        if len(keys) == num_keys:
            return len(keys)

        # Explore the four cardinal directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy

            # Check if the new position is within the grid
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                cell = grid[new_row][new_col]

                # Check if the new position is a wall or a lock without the key
                if cell == "#" or (cell.isupper() and cell.lower() not in keys):
                    continue

                # Check if the new position is a key
                if cell.islower():
                    new_keys = keys + cell
                else:
                    new_keys = keys

                # Check if the new position has been visited before
                if (new_row, new_col, new_keys) not in visited:
                    visited.add((new_row, new_col, new_keys))
                    queue.append((new_row, new_col, new_keys))

    # If all keys cannot be collected, return -1
    return -1
