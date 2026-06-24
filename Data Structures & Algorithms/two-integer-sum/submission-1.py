class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = set()

        for ind, num in enumerate(nums):
            if num in diff:
                return [nums.index(target - num), ind]
            
            diff.add(target - num)
        