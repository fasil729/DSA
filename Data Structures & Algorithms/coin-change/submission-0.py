class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float("infinity")
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for t in range(1, amount + 1):

            for coin in coins:
                if t - coin >= 0:
                    dp[t] = min(dp[t], 1 + dp[t - coin])
        
        return dp[amount] if dp[amount] < inf else -1
            






        

        