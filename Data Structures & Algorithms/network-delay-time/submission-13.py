import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build adjacency list (0-indexed)
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))

        # 2. Initialize distances array
        dist = [float('inf')] * n
        dist[k - 1] = 0
        
        # Min-heap stores tuples of (time_to_reach_node, node)
        min_heap = [(0, k - 1)]

        # 3. Dijkstra's Algorithm
        while min_heap:
            current_time, u = heapq.heappop(min_heap)

            # Prune stale entries (CRITICAL for O((V + E) log V) time complexity)
            # if current_time > dist[u]:
            #     continue

            for v, weight in graph[u]:
                new_time = current_time + weight
                # Relaxation step: update distance if a shorter path is found
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(min_heap, (new_time, v))

        # 4. Return maximum time needed to reach all nodes, or -1 if unreachable
        max_time = max(dist)
        return max_time if max_time != float('inf') else -1