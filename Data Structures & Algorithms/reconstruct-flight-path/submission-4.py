class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        

        res = []
        def dfs(src):
            
            while adj[src]:
                dst = adj[src].popleft()
                dfs(dst)
            res.append(src)
            

        dfs('JFK')
        return res[::-1]
    