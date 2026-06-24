class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        n, m = len(text1), len(text2)

        def dp(i, j):
            if i >= n or j >= m:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dp(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = max(dp(i, j + 1), dp(i + 1, j))
            return memo[(i, j)]
        
        if n == 0 or m == 0:
            return 0
        
        return dp(0, 0)

        