from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Adjacency list using lists instead of sets for lower memory overhead
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # 1. Build adjacency list and compute in-degrees
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # 2. Enqueue all courses with 0 prerequisites
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        order = []

        # 3. Process nodes level-by-level
        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. If order contains all courses, return it; otherwise, a cycle exists
        return order if len(order) == numCourses else []