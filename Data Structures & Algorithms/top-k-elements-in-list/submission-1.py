class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        freq = [[] for _ in range(n)]
        ans = []

        for num, cnt in count.items():
            freq[cnt - 1].append(num)
        
        for ind in range(n - 1, -1, -1):
            if k == 0:
                break
            ans.extend(freq[ind])
            k -= len(freq[ind])
        
        return ans

        


    
        