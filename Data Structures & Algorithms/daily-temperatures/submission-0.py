class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []


        for ind in range(n):
            temp = temperatures[ind]
            while stack and stack[-1][0] < temp:
                _, i = stack.pop()
                output[i] = ind - i
            
            stack.append((temp, ind))
        
        return output


        