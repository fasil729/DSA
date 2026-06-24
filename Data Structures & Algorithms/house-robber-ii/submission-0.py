class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):
        n = len(nums)
        first, second = 0, 0

        for i in range(n - 1, -1, -1):
            temp = second
            second = max(nums[i] + first, second)
            first = temp
        
        return second
        