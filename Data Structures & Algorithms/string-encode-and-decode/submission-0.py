class Solution:
    def __init__(self):
        self.indices = []

    def encode(self, strs: List[str]) -> str:
        ans = ""
        ind = 0
        self.indices = []
        for s in strs:
            ans += s
            ind += len(s)
            self.indices.append(ind)
            
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        i = 0

        for ind in self.indices:
            word = ""
            while i < ind:
                word += s[i]
                i += 1
            ans.append(word)
            
        return ans 

            


