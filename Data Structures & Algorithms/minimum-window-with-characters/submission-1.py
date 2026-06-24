class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        s_dict = defaultdict(int)
        start = 0
        ans = ""
        unique = len(t_dict)
        matches = 0


        for end in range(len(s)):
            char = s[end]
            while start < end and s_dict[s[start]] > t_dict[s[start]]:
                s_dict[s[start]] -= 1
                start += 1

            if s_dict[char] == t_dict[char] - 1:
                matches += 1
            
            s_dict[char] += 1

            if matches == unique:
                leng = end - start + 1
                if not ans or leng < len(ans):
                    ans = s[start:end + 1]
                
                if s_dict[s[start]] == t_dict[s[start]]:
                    matches -= 1
                
                s_dict[s[start]] -= 1
                start += 1
        
        return ans
            
            

