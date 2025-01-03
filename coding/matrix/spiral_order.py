"""
MATRIX SPIRAL PRINT

Given an m x n matrix, 
return all elements of the matrix in spiral order.

"""
# Spiral order
def spiral_order(matrix):
    row_start, row_end = 0, len(matrix) - 1
    column_start, column_end = 0, len(matrix[0]) - 1
    print(row_start, row_end, column_start, column_end)

    order = []
    while row_start <= row_end and column_start <= column_end:

        # right
        for i in range(column_start, column_end + 1):
            order.append(matrix[row_start][i])
        row_start += 1

        # down
        for i in range(row_start, row_end + 1):
            order.append(matrix[i][column_end])
        column_end -= 1

        # left
        if row_start <= row_end:
            for i in range(column_end, column_start - 1, -1):
                order += matrix[row_end][i],
            row_end -= 1

        # up
        if column_start <= column_end:
            for i in range(row_end, row_start - 1, -1):
                order += matrix[i][column_start],
            column_start += 1

    return order


matrix = [[1, 2, 3, 10], [4, 5, 6, 20], [7, 8, 9, 30]]
spiral_order(matrix)

def bfs(self, root: TreeNode) -> list:
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result