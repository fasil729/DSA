from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable_set):
            # Mark the current cell as able to reach the respective ocean
            reachable_set.add((r, c))
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                # The core logic inversion: Water flows UPHILL (or equal height) from the ocean
                if (
                    0 <= nr < rows and 
                    0 <= nc < cols and 
                    (nr, nc) not in reachable_set and 
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, reachable_set)

        # 1. Multi-source start from all horizontal borders
        for c in range(cols):
            dfs(0, c, pacific_reachable)         # Top row (Pacific)
            dfs(rows - 1, c, atlantic_reachable) # Bottom row (Atlantic)

        # 2. Multi-source start from all vertical borders
        for r in range(rows):
            dfs(r, 0, pacific_reachable)         # Left column (Pacific)
            dfs(r, cols - 1, atlantic_reachable) # Right column (Atlantic)

        # 3. Find the intersection (cells that can reach both)
        return [list(cell) for cell in pacific_reachable.intersection(atlantic_reachable)]