class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        prefix_dict = defaultdict(int)
        ans = 0

        for num in nums:
            prefix_dict[prefix] += 1
            prefix += num
            ans += prefix_dict[prefix - k]
        
        return ans