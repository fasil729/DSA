class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
                return 0
        n = len(s)
        seen = [None] * n

        def dp(ind):
            if ind < n and s[ind] == '0':
                return 0
            if ind >= n - 1:
                return 1
            if seen[ind] != None:
                return seen[ind]

            

            seen[ind] = dp(ind + 1)
            seen[ind] += dp(ind + 2) if int(s[ind: ind + 2]) <= 26 else 0
            return seen[ind]
        
        return dp(0)
            


        