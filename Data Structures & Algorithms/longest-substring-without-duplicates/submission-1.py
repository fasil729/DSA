class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        start = 0
        n = len(s)
        ans = 0

        for end in range(n):

            while s[end] in sub:
                sub.remove(s[start])
                start += 1

            ans = max(ans, end - start + 1)
            sub.add(s[end])
        

        return ans
        



        