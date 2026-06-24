class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0

        for price in prices:
            if mini < price:
                profit += price - mini
                mini = price
            else:
                mini = min(price, mini)
        
        return profit
        

        