class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[None] * n for _ in range(m)]

        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1
            if row >= m or col >= n:
                return 0
            if dp[row][col] != None:
                return dp[row][col]
            
            
            dp[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
            return dp[row][col]


        
        return dfs(0, 0)