class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [None] * (n + 1)
        memo[0] = 0

        def dp(num):
            if memo[num] != None:
                return memo[num]
            
            memo[num] = num % 2 + dp(num // 2)
            return memo[num]
        
        for i in range(n + 1):
            dp(i)

        return memo
        