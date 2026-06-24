class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = []

        for i, s in enumerate(strs):
            sorted_str.append((sorted(s), i))
        
        sorted_str.sort()
        _, first_ind = sorted_str[0]

        ans = [ [strs[first_ind]] ]
        for i in range(1, len(strs)):
            s, ind = sorted_str[i] 
            if sorted_str[i - 1][0] == s:
                ans[-1].append(strs[ind])
            else:
                ans.append([ strs[ind] ])
        
        return ans


        