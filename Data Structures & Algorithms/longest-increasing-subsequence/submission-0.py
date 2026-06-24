class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        

        def dp(ind):
            if ind in memo:
                return memo[ind]

            res = 1
            for i in range(ind, n):
                if nums[ind] < nums[i]:
                    res = max(res, 1 + dp(i))
            
            memo[ind] = res
            
            return res
        
        ans = 1
        for ind in range(n):
            ans = max(ans, dp(ind))
        
        return ans


        