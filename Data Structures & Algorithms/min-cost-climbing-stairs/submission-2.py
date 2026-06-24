class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        one, two = 0, 0

        for i in range(n - 1, -1, -1):
            temp = two
            two = cost[i] + min(one, two)
            one = temp
        
        return min(one, two)
        