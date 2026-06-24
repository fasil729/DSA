class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = max(prices)

        for price in prices:
            profit = max(profit, price - mini)
            mini = min(mini, price)
        
        return profit
        