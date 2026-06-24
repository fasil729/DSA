class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, count1, num2, count2 = 0, 0, 0, 0
        n, ans = len(nums), []

        for num in nums:
            if num1 == num or count1 == 0:
                num1 = num
                count1 += 1
            elif num2 == num or count2 == 0:
                num2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        

        if nums.count(num1) > n // 3:
            ans.append(num1)
        
        if nums.count(num2) > n // 3:
            ans.append(num2)

        return ans
        