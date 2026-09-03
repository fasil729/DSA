class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [None] * (n + 1)
        memo[0] = 0
        
        for i in range(1, n + 1):
            memo[i] = i % 2 + memo[i // 2]
            

        return memo
        