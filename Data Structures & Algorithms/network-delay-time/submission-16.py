
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        k -= 1
        visited = [float("infinity") for _ in range(n)]
        heap = [(0, k)]
        
        for u, v, t in times:
            graph[u - 1].append((v - 1, t))

        
        
        print("upper")
        while heap:
            time, node = heapq.heappop(heap)
            if visited[node] != float("infinity"):
                continue

            visited[node] = min(visited[node], time)
            

            for v, t in graph[node]:
                heapq.heappush(heap, (time + t, v))
        print("lower")  
        return max(visited) if max(visited) != float("infinity") else -1
        