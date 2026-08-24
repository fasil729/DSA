class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = max(nums)
        running_sum = 0


        for num in nums:
            running_sum = max(num, running_sum + num)
            max_sum = max(running_sum, max_sum)
        

        return max_sum


        