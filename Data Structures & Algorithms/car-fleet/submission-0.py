class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        stack = sorted([[position[ind], speed[ind]] for ind in range(len(position))])


        while stack:
            pos, sp = stack.pop()
            t = (target - pos) / sp
            while stack:
                if (target - stack[-1][0]) / stack[-1][1] > t:
                    break
                stack.pop()
            
            ans += 1
        
        return ans
        