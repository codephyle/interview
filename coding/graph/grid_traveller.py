"""
GRID TRAVELLER

Say that you are a traveller on a 2D grid. You begin in the 
top-left corner and your goal is to travel to the bottom-right
corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with
dimensions m*n?

tags: dynamic, grid, matrix

Approach:

1. Think about a 1x1 grid. There is only one way to travel.
2. If there is no grid, what are the number of ways? Possibly, 0. correct?
3. Otherwise, we can go one box right, removing a column OR one box down, eliminating a row.
   and we do this recursively
   
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def gridTraveller(m, n):
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    return gridTraveller(m-1, n) + gridTraveller(m, n-1)

print(gridTraveller(2,3))
print(gridTraveller(18,18))
