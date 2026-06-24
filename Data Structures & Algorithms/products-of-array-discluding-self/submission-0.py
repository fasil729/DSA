class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        n = len(nums)

        for num in nums:
            prefix.append(prefix[-1] * num)

        suffix = [1]
        for num in nums[::-1]:
            suffix.append(suffix[-1] * num)
        
        suffix = suffix[::-1]

        ans = []
        for ind in range(n):
            ans.append(prefix[ind] * suffix[ind + 1])

        return ans
