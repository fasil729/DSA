from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
           prerequisites   [[0,1],[1,2]]  3
           indegree     [0, 0, 0]
           graph        [ {}  {0}  {1}]
           queue        []


           order  [2, 1, 0]

        
        
        """



        graph = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        order = []
        for a, b in prerequisites:  
            graph[b].add(a)
            indegree[a] += 1

        queue = deque([c for c in range(numCourses) if indegree[c] == 0])


        while queue:
            course = queue.popleft()  # course 0
            order.append(course)  

            for adj in graph[course]:   # {}    adj 
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
            
        
        return order if len(order) == numCourses else [] # 3  == 3
