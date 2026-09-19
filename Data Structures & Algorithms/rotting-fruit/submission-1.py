from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))

        
        if queue:
            minutes = -1
        

        while queue:
            length = len(queue)

            for _ in range(length):
                row, col = queue.popleft()
                

                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            
            minutes += 1
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        
        return minutes
        



        