"""
Daily temperatures

Given an array of integers representing the daily temperatures, return an array answer such that answer[i] is the number of days
you have to wait after the ith day to get a warmer temperature.

If there is no future day for which this is possible, keep answer[i] == 0 instead.

"""


def daily_temperatures(T):
    ans = [0] * len(T)
    stack = []  # stack of indexes
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)
    return ans


daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
