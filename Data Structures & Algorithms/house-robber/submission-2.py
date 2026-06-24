class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        first, second = 0, 0

        for i in range(n - 1, -1, -1):
            temp = second
            second = max(nums[i] + first, second)
            first = temp
        
        return second
        