from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid_land(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1

        def bfs(start_row: int, start_col: int) -> int:
            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))
            current_area = 0

            while queue:
                r, c = queue.popleft()
                current_area += 1

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid_land(nr, nc) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return current_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))

        return max_area