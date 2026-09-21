class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # # 1. Lock in the edge count property
        if len(edges) != n - 1:
            return False
            
        # Build graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        # 2. Simple DFS just to mark reachable nodes
        def dfs(node):
            if node in visited:
                return  # Just stop exploring this path, no need to return False
                
            visited.add(node)
            for neigh in graph[node]:
                dfs(neigh)
                
        # Start traversal from node 0
        dfs(0)
        
        # 3. If we reached every node, it's connected. 
        # Connected + (n-1) edges = Valid Tree.
        return len(visited) == n