"""
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.

You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0
you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
"""

# ChatGPT verfied solution

# https://leetcode.com/problems/course-schedule/discuss/162743/JavaC%2B%2BPython-BFS-Topological-Sorting-O(N-%2B-E)

from collections import deque, defaultdict

def can_finish(n, prereqs):
    graph = defaultdict(list)
    indegree = [0] * n

    for course, prerequisite in prereqs:
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque()
    for course, degree in enumerate(indegree):
        if degree == 0:
            queue.append(course)

    taken_courses = 0
    while queue:
        course = queue.popleft()
        taken_courses += 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return n == taken_courses

def canFinish(n, prereqs):
    
    graph = defaultdict(list)
    for course, prereq in prereqs:
        graph[prereq].append(course)

    visited = [0] * n

    def dfs(root):
        
        if visited[root] == 1: # currently visiting
            return False
        
        if visited[root] == 2: # already visited
            return True

        visited[course] = 1

        for neigh in graph[root]:
            visited[root] = 2
            if not dfs[neigh]:
                return False

        visited[root] = 2
        return True

    for course in range(n):
        if visited[course] == 0:
            if not dfs(course):
                return False

    return True




assert can_finish(2, [[1, 0]]) == True
assert can_finish(2, [[1, 0], [0, 1]]) == False
