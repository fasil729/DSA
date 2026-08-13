class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [None] * n
        t = 0
        for w in wordDict:
            t = max(t, len(w))

        def dfs(i):
            if i == n:
                return True
            if dp[i] != None:
                return dp[i]
            
            sub = ""
            for j in range(i, min(n, i + t)):
                sub += s[j]
                if sub in wordSet and dfs(j + 1):
                    dp[j] = True
                    return dp[j]
            
            dp[j] = False
            return dp[j]
            

        
        return dfs(0)