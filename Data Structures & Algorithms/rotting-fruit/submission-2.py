from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # 1. Initial pass: Enqueue sources and count targets
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # Early exit: If there are no fresh oranges, it takes 0 minutes
        if fresh_count == 0:
            return 0
            
        minutes = 0
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. Multi-source BFS
        while queue:
            level_size = len(queue)
            rotted_this_minute = False
            
            for _ in range(level_size):
                r, c = queue.popleft()
                
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    
                    # If we find a valid fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2       # Rot it
                        fresh_count -= 1       # Update our tracker
                        queue.append((nr, nc)) # Enqueue for next minute
                        rotted_this_minute = True
                        
            # Only increment time if we actually rotted something this round
            if rotted_this_minute:
                minutes += 1
                
        # 3. Check our tracker instead of rescanning the grid
        return minutes if fresh_count == 0 else -1