class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        pacfic = [[True if r == 0 or c == 0 else None for c in range(Cols)] for r in range(Rows)] 
        atlantic = [[True if r == Rows - 1 or c == Cols - 1 else None for c in range(Cols)] for r in range(Rows)] 
        ans = []

        def is_valid(row, col):
            return 0 <= row < Rows and 0 <= col < Cols

        def dfs(r, c, visited):
            if visited[r][c] != None:
                return visited[r][c]

            visited[r][c] = False
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            height = heights[r][c]
            for r_d, c_d in directions:
                n_r, n_c = r + r_d, c + c_d

                if is_valid(n_r, n_c) and height >= heights[n_r][n_c] and dfs(n_r, n_c, visited):
                    visited[r][c] = True
                    return True
            
            return False
        
        for row in range(Rows):
            for col in range(Cols):
                dfs(row, col, pacfic)
                dfs(row, col, atlantic)
                if atlantic[row][col] == True and pacfic[row][col] == True:
                    ans.append([row, col])
        
        return ans
            
            
        