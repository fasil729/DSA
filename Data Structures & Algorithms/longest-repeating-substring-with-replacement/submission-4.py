class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        start = 0
        maxf = 0
        ans = 0

        for end in range(len(s)):
            count[s[end]] += 1
            maxf = max(maxf, count[s[end]])


            while (end - start + 1) - maxf > k:
                count[s[start]] -= 1
                start += 1
            
            ans = max(ans, (end - start + 1))

        return ans



