from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()
        distance = 0
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        def is_valid_land(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 2147483647
        
        while queue:
            n = len(queue)
            new_queue = deque()
            distance += 1

            for _ in range(n):
                row, col = queue.popleft()
                
                
                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if is_valid_land(nr, nc):
                        new_queue.append((nr, nc))
                        grid[nr][nc] = distance
                        
            
            
            queue = new_queue
