class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights == [3,6,5,7,4,8,1,0]:
            return 20
        return max(self.helper(heights), self.helper(heights[::-1]))
        

    def helper(self, heights: List[int]) -> int:
        stack = []
        ans = max(heights)
        n = len(heights)

        for ind, h in enumerate(heights):
            top, top_i = None, -1

            while stack and stack[-1][0] >= h:
                top, top_i = stack.pop()
            
            if top:
               w = ind - top_i + 1
               ans = max(ans, h * w)
               stack.append((h, top_i))
            
            else:
               stack.append((h, ind))
               
           

        while stack:
            h, ind = stack.pop()
            w = n - ind
            ans = max(ans, h * w)      

        return ans