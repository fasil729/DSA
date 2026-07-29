class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            in_degree[a] += 1
            graph[b].append(a)
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            course = queue.popleft()
            for adj in graph[course]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
        

        return all(in_degree[i] == 0 for i in range(numCourses))

            
            

        