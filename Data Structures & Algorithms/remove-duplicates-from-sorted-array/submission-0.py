class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        n = len(nums)

        while slow < n:
            if fast == n:
                return slow
            if fast == 0 or nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
            
        return n
        