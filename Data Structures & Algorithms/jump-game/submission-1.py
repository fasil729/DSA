class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        n = len(nums)

        for ind, num in enumerate(nums):
            if max_ind >= n - 1:
                return True
            if max_ind < ind:
                return False

            max_ind = max(max_ind, ind + num)
        
        return True

        