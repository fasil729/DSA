class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        s_0 = 0
        s_1 = nums.count(0)
        s_2 = s_1 + nums.count(1)

        for i in range(n):
            if i >= s_2:
                nums[i] = 2
            elif i >= s_1:
                nums[i] = 1
            else:
                nums[i] = 0
        




        