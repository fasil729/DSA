class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left, right = 0, len(heights) - 1

        while left < right:
            diff = right - left
            area = min(heights[left], heights[right]) * diff
            ans = max(ans, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        

        return ans
        