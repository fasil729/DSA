class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        visited = set()
        max_area = 0


        def isValid_index(r, c):
            return 0 <= r < Rows and 0 <= c < Cols and grid[r][c] == 1

        def bfs(row, col):
            
            queue = deque([(row, col)])  
            visited.add((row, col))
            ans = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                curr_row, curr_col = queue.popleft()
                ans += 1
                

                for direc_r, direc_c in directions:
                    new_row, new_col = curr_row + direc_r, curr_col + direc_c
                    if (new_row, new_col) not in visited and isValid_index(new_row, new_col):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                
            
            return ans



        for row in range(Rows):
            for col in range(Cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = bfs(row, col)
                    max_area = max(area, max_area)
        

        return max_area


        
        
        