class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = nums[0]
        curr_max , curr_min = 1, 1

        for num in nums:
            temp = curr_max
            curr_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, temp * num, curr_min * num)

            max_pro = max(max_pro, curr_max)
        
        return max_pro



        