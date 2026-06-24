class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1, i2 = 0, 0
        n, m = len(word1), len(word2)
        ans = ""

        while i1 < n and i2 < m:
            ans += word1[i1]
            ans += word2[i2]
            i1 += 1
            i2 += 1
        
        while i1 < n:
            ans += word1[i1]
            i1 += 1
        
        while i2 < m:
            ans += word2[i2]
            i2 += 1
        

        return ans
        
        
        
        