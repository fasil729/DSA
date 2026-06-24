class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]

        for s in strs:
            i = 0
            while i < len(ans) and i < len(s):
                if s[i] != ans[i]:
                    break
                i += 1
            
            ans = ans[:i]
        
        return ans
        