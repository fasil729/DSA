from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # 1. Enqueue all sources (treasures)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # 2. Process level by level using a single queue
        distance = 1
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                r, c = queue.popleft()
                
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    # In-place mutation inherently prevents revisiting
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                        grid[nr][nc] = distance
                        queue.append((nr, nc))
                        
            distance += 1