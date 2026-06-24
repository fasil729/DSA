class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)
        start = 0
        

        for end in range(len(s2)):
            char = s2[end]
            while start <= end and not s1_dict.get(char, 0):
                if start < end:
                    s1_dict[s2[start]] += 1
                start += 1
            
            if char in s1_dict:
                print(char)
                s1_dict[char] -= 1
        
            if (end - start) + 1 == len(s1):
                return True
        
        return False
        