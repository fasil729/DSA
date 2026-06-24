class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resLen = 0
        residx = 0

        dp = [[False] * n for _ in range(n)] 

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                leng = j-i+1
                if s[i] == s[j] and (leng <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if leng > resLen:
                        resLen = leng
                        residx = i
        
        return s[residx : residx + resLen]

