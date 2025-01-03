"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

"""
from functools import lru_cache


@lru_cache(maxsize=None)
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)


# fibonacci
def climb_stairs_faster(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


climb_stairs(10)
climb_stairs_faster(9)
