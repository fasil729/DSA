class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        sorted_count = sorted(nums_count.items(), key=lambda x: x[1], reverse=True)
        ans = []
        ind = 0

        while ind < k:
            ans.append(sorted_count[ind][0])
            ind += 1

        return ans


    
        