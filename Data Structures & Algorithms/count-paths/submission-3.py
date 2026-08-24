class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[n - 1] = 1


        for row in range(m - 1, -1, -1):
            new_dp = [0] * (n + 1)
            for col in range(n - 1, -1, -1):
                new_dp[col] += dp[col] + new_dp[col + 1]
            
            dp = new_dp
        
        return dp[0]