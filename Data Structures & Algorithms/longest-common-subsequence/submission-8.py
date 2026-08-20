class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # top down
        # memo = {}
        # n, m = len(text1), len(text2)

        # def dp(i, j):
        #     if i >= n or j >= m:
        #         return 0
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     if text1[i] == text2[j]:
        #         memo[(i, j)] = 1 + dp(i + 1, j + 1)
        #     else:
        #         memo[(i, j)] = max(dp(i, j + 1), dp(i + 1, j))

        #     return memo[(i, j)]
        
        
        # return dp(0, 0)


        # bottom up optimized
        
        n, m = len(text1), len(text2)
        prev_dp = {}
        curr_dp = {}

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr_dp[j] = 1 + prev_dp.get(j + 1, 0)
                else:
                   curr_dp[j] = max(curr_dp.get(j + 1, 0) , prev_dp.get(j, 0))

            prev_dp = curr_dp
            curr_dp = {}
        
        return prev_dp[0]





        